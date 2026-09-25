# Archivo: core/backend/ide_core/config/registro_modulos.py
"""Carga y registro de modulos plug-in del IDE."""

import importlib

from fastapi import FastAPI

from ide_core.config.constants import MODULOS_REGISTRADOS
from ide_core.utils.logger import log_sistema


def registrar_modulos(app: FastAPI) -> None:
    """Importa y registra cada modulo declarado en MODULOS_REGISTRADOS."""
    for ruta in MODULOS_REGISTRADOS:
        try:
            modulo = importlib.import_module(ruta)
        except ImportError as exc:
            log_sistema.error("Modulo no disponible: %s (%s)", ruta, exc)
            continue

        registrar = getattr(modulo, "registrar", None)
        if not callable(registrar):
            log_sistema.warning("Modulo sin funcion registrar(): %s", ruta)
            continue

        registrar(app)
        log_sistema.info("Modulo registrado: %s", ruta)
