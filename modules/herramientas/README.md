# Modulo Herramientas

**Equipo responsable**: GRIS
**Version**: 1.0.0

Modulo plug-in del IDE ESP32 que aporta monitor serie, plotter, gestion de
placas y puertos, flasheo de firmware y certificados SSL/TLS.

## Estructura

```
modules/herramientas/
|-- backend/               # Paquete Python: herramientas_backend
|   |-- herramientas_backend/
|   |   |-- modulo.py      # API publica: registrar(app)
|   |   |-- routes.py
|   |   |-- config/, models/, controllers/, utils/
|   `-- pyproject.toml
|-- frontend/              # Paquete Dart: herramientas_ui
|   |-- lib/
|   |   |-- herramientas_ui.dart
|   |   |-- modulo_herramientas.dart   # Implementa ModuloIde
|   |   `-- ui/, servicios/
|   `-- pubspec.yaml
`-- docs/
```

## Registro

- **Backend**: el core lo carga via `MODULOS_REGISTRADOS` en
  `ide_core/config/constants.py`.
- **Frontend**: `apps/ide/lib/nucleo/registro_modulos.dart` agrega una
  instancia de `ModuloHerramientas()`.

## Pruebas

```bash
# Backend (desde la raiz del monorepo con venv activado)
cd modules/herramientas/backend
pytest pruebas/ -v

# Frontend
cd modules/herramientas/frontend
flutter test
```