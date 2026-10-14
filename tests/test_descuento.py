import pytest
from descuento import descuento


def test_descuento_correcto():
    assert descuento(500, 20) == 400


def test_descuento_cero():
    assert descuento(500, 0) == 500


def test_descuento_total():
    assert descuento(500, 100) == 0


def test_precio_negativo():
    with pytest.raises(ValueError):
        descuento(-100, 20)


def test_porcentaje_invalido():
    with pytest.raises(ValueError):
        descuento(500, 120)


def test_precio_no_numerico():
    with pytest.raises(TypeError):
        descuento("quinientos", 20)