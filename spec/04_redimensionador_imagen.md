# Spec 04: Redimensionador de Imágenes

## Objetivo
Crear una aplicación de escritorio en Python que reduzca el tamaño de una foto (ancho máximo) y la guarde como JPG, usando una interfaz gráfica sencilla.

## Alcance
- **Entrada:** Ruta de una imagen (.png, .jpg, .jpeg).
- **Salida:** Nueva imagen con sufijo `_pequeña.jpg`.
- **Lógica:** Librería `Pillow` para abrir, redimensionar y guardar.
- **Ubicación:** `app/redimensionador_imagen/`.
- **GUI:** `customtkinter` para la interfaz de escritorio.

## Pasos
1. Crear `requirements.txt`.
2. Validar rutas en `core.py`.
3. Redimensionar en `core.py`.
4. Interfaz en `gui.py`.
5. Pruebas en `tests/`.

## Riesgos
- Imágenes PNG con transparencia pierden el fondo al pasar a JPG.
- **Mitigación:** Poner fondo blanco antes de guardar.
- **Seguridad:** Validar rutas con `pathlib`.
