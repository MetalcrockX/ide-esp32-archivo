# Archivo: modules/herramientas/backend/herramientas_backend/controllers/report.py
"""Reportes del modulo Herramientas."""

from ide_core.models.base import ejecutar


def resumen_flash() -> dict:
    """Obtiene el resumen de operaciones de flasheo realizadas."""
    filas = ejecutar(
        "SELECT COUNT(*) AS total, SUM(exitoso) AS exitosos "
        "FROM herramientas_historial_flash"
    )
    if not filas:
        return {"total": 0, "exitosos": 0, "fallidos": 0}
    total = filas[0]["total"] or 0
    exitosos = filas[0]["exitosos"] or 0
    return {"total": total, "exitosos": exitosos, "fallidos": total - exitosos}
