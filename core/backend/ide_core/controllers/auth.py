# Archivo: core/backend/ide_core/controllers/auth.py
"""Logica de autenticacion del IDE."""

from ide_core.controllers.exceptions import ErrorAutorizacion
from ide_core.controllers.validator import normalizar_usuario
from ide_core.models.usuario import buscar_por_usuario, crear_usuario
from ide_core.utils.logger import log_sistema
from ide_core.utils.security import generar_hash, verificar_hash


def registrar_usuario(usuario: str, password: str, rol: str = "operador") -> int:
    """Registra un nuevo usuario en el sistema."""
    usuario = normalizar_usuario(usuario)
    if buscar_por_usuario(usuario):
        raise ErrorAutorizacion("El usuario ya existe.")
    hash_ = generar_hash(password)
    nuevo_id = crear_usuario(usuario, hash_, rol)
    log_sistema.info("Usuario registrado: %s (id=%s)", usuario, nuevo_id)
    return nuevo_id


def autenticar(usuario: str, password: str) -> dict:
    """Autentica a un usuario verificando sus credenciales."""
    usuario = normalizar_usuario(usuario)
    registro = buscar_por_usuario(usuario)
    if not registro or not verificar_hash(password, registro["password_hash"]):
        raise ErrorAutorizacion("Credenciales invalidas.")
    log_sistema.info("Autenticacion exitosa: %s", usuario)
    return {
        "id": registro["id"],
        "usuario": registro["usuario"],
        "rol": registro["rol"],
    }
