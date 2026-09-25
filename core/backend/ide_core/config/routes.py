# Archivo: core/backend/ide_core/config/routes.py
"""Rutas base del IDE."""

from fastapi import APIRouter

from ide_core.config.constants import NOMBRE_CORE, PREFIJO_API, VERSION_CORE
from ide_core.models.modulo import listar_modulos


def _salud() -> dict:
    return {"estado": "ok", "app": NOMBRE_CORE, "version": VERSION_CORE}


def _modulos() -> dict:
    return {"modulos": listar_modulos()}


def configurar_rutas_base() -> APIRouter:
    """Configura y retorna el enrutador de rutas base del core."""
    router = APIRouter(prefix=PREFIJO_API, tags=["core"])
    router.add_api_route("/salud", _salud, methods=["GET"])
    router.add_api_route("/modulos", _modulos, methods=["GET"])
    return router
