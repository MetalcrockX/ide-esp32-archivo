"""Pruebas basicas del core."""

from ide_core.config.constants import PREFIJO_API, VERSION_CORE


def test_version_core_definida():
    assert VERSION_CORE


def test_prefijo_api():
    assert PREFIJO_API == "/api/v1"
