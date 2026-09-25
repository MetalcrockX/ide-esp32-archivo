# Archivo: modules/herramientas/backend/herramientas_backend/models/dispositivo.py
"""Historial de flasheo del modulo Herramientas."""

from ide_core.models.base import ejecutar, ejecutar_mutacion


def registrar_flash(
    dispositivo_id: int, archivo: str, exitoso: bool, salida: str = ""
) -> int:
    """Registra una operacion de flasheo en la base de datos."""
    return ejecutar_mutacion(
        "INSERT INTO herramientas_historial_flash "
        "(dispositivo_id, archivo, exitoso, salida) VALUES (?, ?, ?, ?)",
        (dispositivo_id, archivo, int(exitoso), salida),
    )


def historial_por_dispositivo(dispositivo_id: int) -> list[dict]:
    """Obtiene el historial de flasheo para un dispositivo especifico."""
    return ejecutar(
        "SELECT * FROM herramientas_historial_flash "
        "WHERE dispositivo_id = ? ORDER BY fecha DESC",
        (dispositivo_id,),
    )
