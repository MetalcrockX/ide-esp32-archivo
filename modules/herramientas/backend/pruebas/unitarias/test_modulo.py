"""Pruebas basicas del modulo."""

from herramientas_backend.modulo import NOMBRE_MODULO, VERSION_MODULO


def test_modulo_identificado():
    assert NOMBRE_MODULO == "herramientas"
    assert VERSION_MODULO
