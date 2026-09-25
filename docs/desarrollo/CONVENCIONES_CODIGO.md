# Convenciones de Codigo

## Python

- Formato: **black** (line-length=100).
- Imports: **isort** (perfil black).
- Estilo: **pylint** >= 8.0.
- **Imports absolutos con nombre de paquete unico**:
  - Core: `from ide_core.x import y`
  - Modulo: `from herramientas_backend.x import y`
- **PROHIBIDO crear `__init__.py`** (namespace packages PEP 420).
- Punto de entrada publico por backend: archivo `modulo.py` con
  `def registrar(app: FastAPI) -> None`.
- **Dependencias**: agregar siempre a `requirements.txt` (raiz), nunca crear
  requirements locales en `core/` ni en `modules/`.

## Dart

- Formato: `dart format` + `flutter analyze`.
- Widgets preferentemente `const`.
- Cada modulo de frontend expone **una unica clase publica** que implementa
  `ModuloIde` (nombre: `Modulo<Nombre>`).
- Los paquetes Dart de modulos dependen de `ide_core` via `path:`.

## SQL

- Un archivo por modulo: `sql/02_schema_<modulo>.sql`.
- Los prefijos `NN_` determinan el orden de aplicacion.