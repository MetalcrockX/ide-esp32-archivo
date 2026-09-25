# Archivo: core/backend/ide_core/utils/security.py
"""
Hash de contrasenas con bcrypt directo.

NOTA: passlib esta obsoleto e incompatible con bcrypt >= 4.1.
Se usa bcrypt directamente (gensalt / hashpw / checkpw).
"""

import bcrypt


def generar_hash(password: str) -> str:
    """Genera un hash bcrypt de la contrasena (incluye salt)."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")


def verificar_hash(password: str, hash_guardado: str) -> bool:
    """Verifica una contrasena contra un hash bcrypt almacenado."""
    try:
        return bcrypt.checkpw(
            password.encode("utf-8"),
            hash_guardado.encode("utf-8"),
        )
    except (ValueError, TypeError):
        return False
