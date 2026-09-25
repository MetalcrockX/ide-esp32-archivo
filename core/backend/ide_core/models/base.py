# Archivo: core/backend/ide_core/models/base.py
"""Acceso a datos compartido."""

from typing import Any

from ide_core.db.connection import conexion


def ejecutar(sql: str, parametros: tuple = ()) -> list[dict[str, Any]]:
    """Ejecuta una consulta SQL de lectura y retorna los registros como lista de diccionarios."""
    with conexion() as conn:
        cursor = conn.execute(sql, parametros)
        return [dict(f) for f in cursor.fetchall()]


def ejecutar_mutacion(sql: str, parametros: tuple = ()) -> int:
    """Ejecuta una consulta SQL de escritura y retorna el lastrowid o rowcount."""
    with conexion() as conn:
        cursor = conn.execute(sql, parametros)
        return cursor.lastrowid or cursor.rowcount
