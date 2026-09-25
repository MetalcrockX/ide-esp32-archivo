# Archivo: core/backend/ide_core/utils/logger.py
"""Logger compartido del IDE."""

import logging
import sys

from ide_core.config.constants import NOMBRE_CORE, RUTA_LOG


def _crear_logger() -> logging.Logger:
    logger = logging.getLogger(NOMBRE_CORE)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    fmt = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    consola = logging.StreamHandler(sys.stdout)
    consola.setFormatter(fmt)
    logger.addHandler(consola)

    try:
        RUTA_LOG.parent.mkdir(parents=True, exist_ok=True)
        archivo = logging.FileHandler(RUTA_LOG, encoding="utf-8")
        archivo.setFormatter(fmt)
        logger.addHandler(archivo)
    except OSError:
        pass

    return logger


log_sistema = _crear_logger()
