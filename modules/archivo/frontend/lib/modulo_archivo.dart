import 'package:flutter/material.dart';
// Aquí deberás importar el http package para conectar con tu backend de FastAPI.

class ModuloArchivo {
  // Las plantillas se inyectarán en el editor de texto principal del IDE
  static const String plantillaBlink = '''
void setup() {
  pinMode(2, OUTPUT);
}
void loop() {
  digitalWrite(2, HIGH);
  delay(1000);
  digitalWrite(2, LOW);
  delay(1000);
}
''';

  static const String plantillaTelemetria = '''
#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>
#include <Adafruit_SSD1306.h>
#include <ArduinoJson.h>

// Configuración de red y sensores para telemetría MQTT
void setup() {
  Serial.begin(115200);
  // Inicialización de OLED, DHT y red
}

void loop() {
  // Lógica de telemetría y deadbanding
}
''';

  // Este método construye la sección de tu menú para que el equipo GRIS lo integre en el shell
  Widget construirMenuArchivo(BuildContext context, Function(String) onUpdateEditor) {
    return SubmenuButton(
      menuChildren: <Widget>[
        MenuItemButton(
          onPressed: () => onUpdateEditor(""),
          child: const Text('Nuevo'),
        ),
        MenuItemButton(
          onPressed: () {
            // Lógica para abrir selector de archivos del OS y llamar a /api/archivo/leer
          },
          child: const Text('Abrir...'),
        ),
        SubmenuButton(
          menuChildren: [
            MenuItemButton(
              onPressed: () => onUpdateEditor(plantillaBlink),
              child: const Text('Blink ESP32'),
            ),
            MenuItemButton(
              onPressed: () => onUpdateEditor(plantillaTelemetria),
              child: const Text('Telemetría IoT (MQTT, DHT11, SSD1306)'),
            ),
          ],
          child: const Text('Ejemplos'),
        ),
        MenuItemButton(
          onPressed: () {
             // Lógica para llamar a /api/archivo/guardar con FastAPI
          },
          child: const Text('Guardar'),
        ),
      ],
      child: const Text('Archivo'),
    );
  }
}
