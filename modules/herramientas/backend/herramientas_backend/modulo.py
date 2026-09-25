# Archivo: modules/herramientas/backend/herramientas_backend/modulo.py
"""
Punto de entrada publico del modulo Herramientas.

El core lo importa como:
    from herramientas_backend.modulo import registrar
"""

from fastapi import FastAPI
from herramientas_backend.routes import router

NOMBRE_MODULO = "herramientas"
VERSION_MODULO = "1.0.0"


def registrar(app: FastAPI) -> None:
    """Registra las rutas del modulo en la app del IDE."""
    app.include_router(router)
