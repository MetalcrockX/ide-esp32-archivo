# Archivo: core/backend/ide_core/models/usuario.py
"""Modelo de usuarios del IDE."""

from ide_core.models.base import ejecutar, ejecutar_mutacion


def crear_usuario(usuario: str, password_hash: str, rol: str = "operador") -> int:
    """Crea un nuevo usuario en la base de datos."""
    return ejecutar_mutacion(
        "INSERT INTO usuarios (usuario, password_hash, rol) VALUES (?, ?, ?)",
        (usuario, password_hash, rol),
    )


def buscar_por_usuario(usuario: str) -> dict | None:
    """Busca un usuario por su nombre y retorna su registro."""
    filas = ejecutar("SELECT * FROM usuarios WHERE usuario = ?", (usuario,))
    return filas[0] if filas else None
