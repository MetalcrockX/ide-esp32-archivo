# Archivo: modules/herramientas/backend/herramientas_backend/controllers/arduino.py
"""Controlador de Arduino CLI."""

import shutil
import subprocess
from dataclasses import asdict, dataclass

from herramientas_backend.config.constants import COMANDO_ARDUINO_CLI

from ide_core.utils.logger import log_sistema


@dataclass
class ResultadoCli:
    """Resultado de ejecucion de arduino-cli."""
    exitoso: bool
    salida: str
    error: str

    def a_dict(self) -> dict:
        """Convierte el resultado a diccionario."""
        return asdict(self)


def _ruta_binario() -> str:
    """Obtiene la ruta del binario arduino-cli."""
    return shutil.which(COMANDO_ARDUINO_CLI) or COMANDO_ARDUINO_CLI


def ejecutar_cli(*args: str, timeout: int = 60) -> ResultadoCli:
    """Ejecuta un comando de arduino-cli con parametros opcionales."""
    try:
        proceso = subprocess.run(
            [_ruta_binario(), *args],
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
        return ResultadoCli(
            proceso.returncode == 0, proceso.stdout.strip(), proceso.stderr.strip()
        )
    except FileNotFoundError:
        log_sistema.error("arduino-cli no encontrado.")
        return ResultadoCli(False, "", "arduino-cli no encontrado.")
    except subprocess.TimeoutExpired:
        return ResultadoCli(False, "", "Tiempo de espera agotado.")


def obtener_version() -> dict:
    """Obtiene la version instalada de arduino-cli."""
    return ejecutar_cli("version").a_dict()


def listar_placas() -> dict:
    """Lista las placas conectadas detectadas por arduino-cli."""
    return ejecutar_cli("board", "list", "--format", "json").a_dict()
