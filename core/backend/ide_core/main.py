# Archivo: core/backend/ide_core/main.py
"""
PUNTO DE ENTRADA UNICO del backend del IDE.

Ejecucion:
    cd core/backend
    python -m ide_core.main
"""

import sys

from ide_core.config.setup import app


def main() -> int:
    """Punto de entrada principal del backend."""
    if not app.establecer_conexion():
        return 1
    app.iniciar_app(recargar=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
