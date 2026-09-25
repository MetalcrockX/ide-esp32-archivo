# Archivo: core/backend/ide_core/controllers/exceptions.py
"""Excepciones comunes del IDE."""


class ErrorAplicacion(Exception):
    """Error base."""


class ErrorValidacion(ErrorAplicacion):
    """Error de validacion de datos."""


class ErrorAutorizacion(ErrorAplicacion):
    """Error de autorizacion o autenticacion."""


class ErrorNoEncontrado(ErrorAplicacion):
    """Error de recurso no encontrado."""
