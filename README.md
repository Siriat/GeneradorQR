# Generador QR

Aplicacion de escritorio sencilla para Windows que genera un codigo QR a partir de una URL o cualquier texto y lo guarda como imagen `.png`.

## Descargar la version portable

Si solo quieres usar el programa, descarga `GeneradorQR.exe` desde GitHub Releases.


## Como usar la aplicacion

1. Abre `GeneradorQR.exe`.
2. Escribe una URL o cualquier texto.
3. Pulsa `Generar QR`.
4. El QR aparecera en la ventana.
5. La imagen `.png` se guardara en la misma carpeta donde este el programa.

## Nombre del archivo generado

La aplicacion usa el texto ingresado como base para el nombre del archivo.

Por ejemplo, si escribes:

```text
https://ejemplo.com/prueba
```

El archivo se guardara con un nombre parecido a:

```text
https___ejemplo.com_prueba.png
```

Esto ocurre porque Windows no permite ciertos caracteres en los nombres de archivo, asi que el programa los reemplaza automaticamente para evitar errores al guardar.

## Requisitos para trabajar con el codigo fuente

Si quieres ejecutar o compilar el proyecto desde el codigo fuente, necesitas:

- Windows 10 u 11
- Python 3.11 o superior
- conexion a internet para instalar dependencias

## Preparar el entorno de desarrollo

Si vas a trabajar con el proyecto desde cero en una PC nueva, sigue estos pasos:

### 1. Instalar Python 3.11

Descargalo desde la pagina oficial:

`https://www.python.org/downloads/windows/`

### 2. Descargar el proyecto desde GitHub

Puedes descargar el repositorio como ZIP y descomprimirlo en cualquier carpeta.

## Ejecutar la app desde el codigo fuente

Para abrir la aplicacion desde el codigo fuente, haz doble clic en:

```text
run.bat
```

## Estructura del proyecto

- `app.py`: aplicacion principal
- `run.bat`: abre la app desde el codigo fuente sin mostrar consola
- `build.bat`: genera la version portable `.exe`
- `requirements.txt`: dependencias necesarias para ejecutar y compilar el proyecto

Archivos generados automaticamente:

- `build/`: archivos temporales del proceso de compilacion
- `dist/`: carpeta donde queda el ejecutable final
- `*.spec`: archivo generado por PyInstaller
- `*.png`: QRs creados por la aplicacion

Esos archivos no hace falta subirlos a GitHub.

## Compilar la version portable

Si quieres generar la version portable para compartirla, haz doble clic en:

```text
build.bat
```

Al terminar, el ejecutable quedara en:

```text
dist\GeneradorQR.exe
```

Ese archivo es el que puedes subir a GitHub Releases para que otras personas lo descarguen directamente.
