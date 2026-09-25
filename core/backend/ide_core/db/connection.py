# Archivo: core/backend/ide_core/db/connection.py
"""Pool de conexiones SQLite del IDE."""

import sqlite3
from contextlib import contextmanager
from pathlib import Path

from ide_core.config.constants import DIRECTORIO_SQL, RUTA_BD
from ide_core.config.database import asegurar_directorios
from ide_core.utils.logger import log_sistema


class ErrorConexion(Exception):
    """Error controlado de conexion."""


_POOL_ACTIVO: bool = False


def init_pool() -> None:
    """Inicializa el pool de conexiones SQLite creando directorios y validando conexion."""
    global _POOL_ACTIVO
    try:
        asegurar_directorios()
        conn = sqlite3.connect(RUTA_BD)
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.execute("PRAGMA journal_mode = WAL;")
        conn.close()
        _POOL_ACTIVO = True
        log_sistema.info("Pool SQLite listo: %s", RUTA_BD)
    except sqlite3.Error as exc:
        _POOL_ACTIVO = False
        raise ErrorConexion(f"No se pudo inicializar SQLite: {exc}") from exc


def get_conn() -> sqlite3.Connection:
    """Obtiene una conexion activa a la base de datos."""
    if not _POOL_ACTIVO and not Path(RUTA_BD).exists():
        raise ErrorConexion("El pool no ha sido inicializado.")
    try:
        conn = sqlite3.connect(RUTA_BD)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn
    except sqlite3.Error as exc:
        raise ErrorConexion(f"No se pudo abrir la conexion: {exc}") from exc


@contextmanager
def conexion():
    """Context manager para manejar transacciones de base de datos."""
    conn = get_conn()
    try:
        yield conn
        conn.commit()
    except sqlite3.Error:
        conn.rollback()
        raise
    finally:
        conn.close()


def aplicar_esquemas_completos() -> None:
    """Aplica todos los scripts SQL en orden lexico."""
    if not DIRECTORIO_SQL.exists():
        log_sistema.warning("Directorio SQL no encontrado: %s", DIRECTORIO_SQL)
        return
    archivos = sorted(DIRECTORIO_SQL.glob("*.sql"))
    with conexion() as conn:
        for archivo in archivos:
            conn.executescript(archivo.read_text(encoding="utf-8"))
            log_sistema.info("Esquema aplicado: %s", archivo.name)
