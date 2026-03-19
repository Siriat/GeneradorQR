import sys
import tkinter as tk
from pathlib import Path
import re

import qrcode
from PIL import Image, ImageTk


BASE_DIR = Path(getattr(sys, "_MEIPASS", Path(__file__).parent))
OUTPUT_DIR = Path.cwd() if getattr(sys, "frozen", False) else Path(__file__).parent


def resource_path(*parts: str) -> Path:
    return BASE_DIR.joinpath(*parts)


def build_output_path(data: str) -> Path:
    safe_name = re.sub(r'[<>:"/\\|?*]', "_", data.strip())
    safe_name = re.sub(r"\s+", " ", safe_name).strip(" .")
    if not safe_name:
        safe_name = "qr_output"
    return OUTPUT_DIR / f"{safe_name}.png"


def build_qr_image(data: str):
    return qrcode.make(data)


def save_qr(data: str, output_file: Path | None = None) -> Path:
    if output_file is None:
        output_file = build_output_path(data)
    image = build_qr_image(data)
    image.save(output_file)
    return output_file


def apply_window_icon(root: tk.Tk) -> None:
    icon_png = resource_path("assets", "icon.png")
    icon_ico = resource_path("assets", "icon.ico")

    if sys.platform.startswith("win") and icon_ico.exists():
        root.iconbitmap(default=str(icon_ico.resolve()))
        return

    if icon_png.exists():
        icon_image = tk.PhotoImage(file=str(icon_png))
        root.iconphoto(True, icon_image)
        root._icon_image = icon_image


def generate_qr() -> None:
    data = url_var.get()
    output_file = save_qr(data)

    preview_image = Image.open(output_file).resize((280, 280))
    tk_image = ImageTk.PhotoImage(preview_image)
    preview_label.configure(image=tk_image, text="")
    preview_label.image = tk_image
    status_var.set(f"QR guardado en: {output_file}")


def main() -> None:
    global root, url_var, status_var, preview_label

    if len(sys.argv) > 1:
        output_path = save_qr(sys.argv[1])
        print(output_path)
        return

    root = tk.Tk()
    root.title("Generador QR")
    root.geometry("380x470")
    root.resizable(False, False)
    root.configure(padx=18, pady=18)
    apply_window_icon(root)

    url_var = tk.StringVar()
    status_var = tk.StringVar(value="Escribe una direccion y pulsa Generar.")

    title_label = tk.Label(root, text="URL o texto")
    title_label.pack(anchor="w")

    entry = tk.Entry(root, textvariable=url_var, width=48)
    entry.pack(fill="x", pady=(6, 12))
    entry.focus()

    generate_button = tk.Button(root, text="Generar QR", command=generate_qr)
    generate_button.pack(fill="x")

    preview_label = tk.Label(
        root,
        text="Aqui aparecera el QR",
        width=280,
        height=18,
        relief="solid",
        bd=1,
    )
    preview_label.pack(fill="both", expand=True, pady=16)

    status_label = tk.Label(root, textvariable=status_var, justify="left", wraplength=340)
    status_label.pack(anchor="w", pady=(0, 10))

    root.mainloop()


if __name__ == "__main__":
    main()
