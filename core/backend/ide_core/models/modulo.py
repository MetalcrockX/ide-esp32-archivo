# Archivo: core/backend/ide_core/models/modulo.py
"""Modelo del registro de modulos instalados."""

from ide_core.models.base import ejecutar, ejecutar_mutacion


def registrar_modulo(nombre: str, version: str) -> int:
    """Registra o actualiza un modulo en la base de datos."""
    return ejecutar_mutacion(
        "INSERT OR REPLACE INTO modulos_instalados (nombre, version) VALUES (?, ?)",
        (nombre, version),
    )


def listar_modulos() -> list[dict]:
    """Lista todos los modulos instalados ordenados por nombre."""
    return ejecutar(
        "SELECT nombre, version, activo FROM modulos_instalados ORDER BY nombre"
    )
