# Archivo: core/backend/ide_core/controllers/validator.py
"""Validaciones y normalizaciones."""

import re

from ide_core.controllers.exceptions import ErrorValidacion

PATRON_USUARIO = re.compile(r"^[a-zA-Z0-9_.-]{3,32}$")


def normalizar_usuario(usuario: str) -> str:
    """Normaliza y valida el nombre de usuario."""
    usuario = usuario.strip().lower()
    if not PATRON_USUARIO.match(usuario):
        raise ErrorValidacion("Nombre de usuario invalido.")
    return usuario
