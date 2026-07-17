import pytest
from PIL import Image
from core import validar_ruta, redimensionar_imagen, ErrorValidacion

def test_archivo_no_existe(tmp_path):
    with pytest.raises(ErrorValidacion, match="no existe"):
        validar_ruta(str(tmp_path / "x.jpg"), str(tmp_path / "y.jpg"))

def test_extension_mala(tmp_path):
    txt = tmp_path / "dato.txt"
    txt.write_text("hola")
    with pytest.raises(ErrorValidacion, match="Solo se permiten"):
        validar_ruta(str(txt), str(tmp_path / "out.jpg"))

def test_redimensionar_ok(tmp_path):
    entrada = tmp_path / "foto.png"
    salida = tmp_path / "foto_pequeña.jpg"

    img = Image.new("RGB", (1600, 900), color=(255, 0, 0))
    img.save(entrada)

    redimensionar_imagen(str(entrada), str(salida), ancho_max=800)

    assert salida.exists()
    result = Image.open(salida)
    assert result.width == 800
    result.close()
