import os
from pathlib import Path
from PIL import Image

class ErrorValidacion(Exception):
    pass

class ErrorImagen(Exception):
    pass

def validar_ruta(ruta_entrada, ruta_salida):
    # Resolver rutas absolutas
    entrada = Path(ruta_entrada).resolve()
    salida = Path(ruta_salida).resolve()

    if not entrada.exists():
        raise ErrorValidacion("El archivo no existe.")

    if entrada.suffix.lower() not in [".png", ".jpg", ".jpeg"]:
        raise ErrorValidacion("Solo se permiten PNG o JPG.")

    return entrada, salida

def redimensionar_imagen(ruta_entrada, ruta_salida, ancho_max=800):
    entrada, salida = validar_ruta(ruta_entrada, ruta_salida)

    if ancho_max < 100:
        raise ErrorValidacion("El ancho mínimo es 100 px.")

    try:
        imagen = Image.open(entrada)

        # Reducir solo si la foto es más ancha que el límite
        if imagen.width > ancho_max:
            alto_nuevo = int(imagen.height * (ancho_max / imagen.width))
            imagen = imagen.resize((ancho_max, alto_nuevo))

        # JPG no guarda transparencia: fondo blanco
        if imagen.mode in ("RGBA", "P"):
            fondo = Image.new("RGB", imagen.size, (255, 255, 255))
            if imagen.mode == "P":
                imagen = imagen.convert("RGBA")
            fondo.paste(imagen, mask=imagen.split()[3])
            imagen = fondo
        elif imagen.mode != "RGB":
            imagen = imagen.convert("RGB")

        imagen.save(salida, "JPEG", quality=80)
        imagen.close()
    except Exception as e:
        raise ErrorImagen("No se pudo procesar la imagen: " + str(e))
