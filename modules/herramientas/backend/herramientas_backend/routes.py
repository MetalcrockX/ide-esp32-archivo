# Archivo: modules/herramientas/backend/herramientas_backend/routes.py
"""Rutas del modulo Herramientas."""

from fastapi import APIRouter
from herramientas_backend.controllers.arduino import listar_placas, obtener_version
from herramientas_backend.controllers.puerto import listar_puertos
from herramientas_backend.controllers.report import resumen_flash

from ide_core.config.constants import PREFIJO_API

router = APIRouter(prefix=f"{PREFIJO_API}/herramientas", tags=["herramientas"])

router.add_api_route("/puertos", listar_puertos, methods=["GET"])
router.add_api_route("/arduino/version", obtener_version, methods=["GET"])
router.add_api_route("/arduino/placas", listar_placas, methods=["GET"])
router.add_api_route("/reportes/flash", resumen_flash, methods=["GET"])
