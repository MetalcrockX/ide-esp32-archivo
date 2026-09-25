# Archivo: core/backend/ide_core/config/database.py
"""Configuracion de la base de datos local del IDE."""

from pathlib import Path

from ide_core.config.constants import DIRECTORIO_DATOS, RUTA_BD, RUTA_LOG


def asegurar_directorios() -> None:
    """Asegura que los directorios de datos y logs existan."""
    Path(DIRECTORIO_DATOS).mkdir(parents=True, exist_ok=True)
    Path(RUTA_LOG).parent.mkdir(parents=True, exist_ok=True)


RUTA_DB = RUTA_BD
DIALECTO = "sqlite"
