# Archivo: modules/herramientas/backend/herramientas_backend/config/constants.py
"""Constantes del modulo Herramientas."""

COMANDO_ARDUINO_CLI = "arduino-cli"

VELOCIDADES_PERMITIDAS = [
    9600,
    19200,
    38400,
    57600,
    115200,
    230400,
    460800,
    921600,
]
VELOCIDAD_DEFECTO = 115200
TIMEOUT_PUERTO = 5

CORE_ESP32 = "esp32:esp32"
PLACA_OBJETIVO = "esp32:esp32:esp32s3"
