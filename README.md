# IDE ESP32 (Monorepo)

**Equipo inicial**: GRIS | **Version**: 6.0 | **Fecha**: 24 sep. 2026

Monorepo del IDE a la medida para ESP32-S31. El **IDE es el producto**;
`herramientas` es **un modulo plug-in** entre varios que equipos distintos
aportaran.

## Arquitectura

| Capa | Ubicacion | Responsable |
|------|-----------|-------------|
| Shell del IDE (UI) | `apps/ide` | GRIS (base) |
| Core backend (API gateway) | `core/backend` | GRIS (base) |
| Core frontend (layout, temas) | `core/frontend` | GRIS (base) |
| Modulos plug-in | `modules/<nombre>` | Cada equipo |
| Contratos compartidos | `shared/contratos` | Todos |
| Esquema SQL | `sql` | Todos |
| Dependencias | `requirements*.txt` (raiz) | Todos |

## Puntos de entrada (SOLO DOS)

| Componente | Comando |
|------------|---------|
| **IDE (Flutter)** | `cd apps/ide && flutter run -d chrome` |
| **Backend (FastAPI)** | `cd core/backend && python -m ide_core.main` |

No hay mas entry points. Los modulos se registran dentro de estos dos.

## Estructura

`
ide-esp32/
   apps/ide/                       # Shell Flutter (UNICO entry point UI)
         lib/
            main.dart               # Punto de entrada
            nucleo/registro_modulos.dart
   core/
      backend/ide_core/           # FastAPI base + registro de modulos
         main.py                 # Punto de entrada backend
         config/
         db/
         models/
         controllers/
         utils/
      frontend/                   # Dart lib base (layout, temas)
         lib/ide_core.dart
         modules/
         herramientas/               # Modulo del equipo GRIS
            backend/herramientas_backend/
            frontend/
README.md
   shared/contratos/               # Contratos JSON FE/BE
   sql/                            # Esquema por modulo
   docs/
   requirements.txt                # Dependencias de produccion (RAIZ)
   requirements-dev.txt            # Dependencias de desarrollo (RAIZ)
   .github/
`

## Instalacion

### 1. Crear y activar el entorno virtual (RAIZ)

`bash
cd ide-esp32
python -m venv venv

# Windows
venv\Scripts\Activate.ps1

# Linux / macOS
source venv/bin/activate
`

### 2. Instalar dependencias (RAIZ)

`bash
pip install -r requirements-dev.txt
`

### 3. Instalar paquetes del monorepo como editables

`bash
# Core
cd core/backend
pip install -e .

# Modulo Herramientas
cd ../../modules/herramientas/backend
pip install -e .

# Volver a la raiz
cd ../../..
`

### 4. Arrancar

`bash
# Backend (terminal 1)
cd core/backend
python -m ide_core.main

# IDE (terminal 2)
cd apps/ide
flutter pub get
flutter run -d chrome          # web
flutter run -d windows         # desktop (Windows)
flutter run -d macos           # desktop (macOS)
flutter run -d linux           # desktop (Linux)
`

## Multiplataforma

La shell del IDE esta preparada para escritorio y web. Para habilitar los
targets de escritorio (una sola vez por maquina):

`bash
flutter config --enable-windows-desktop
flutter config --enable-macos-desktop
flutter config --enable-linux-desktop
`

## Reglas estrictas

1. **NO se permiten archivos `__init__.py`** (namespace packages PEP 420).
2. **Imports Python absolutos con nombre de paquete unico**:
   - `from ide_core.config.constants import X`
   - `from herramientas_backend.controllers.x import y`
3. **Dependencias centralizadas en la raiz**: no crear
   `requirements.txt` dentro de `core/` ni de `modules/`.
4. Cada modulo expone **un unico punto de entrada publico**:
   - Backend: `modulo.py` con `registrar(app)`.
   - Frontend: `modulo_<nombre>.dart` implementando `ModuloIde`.
5. Contratos FE/BE viven en `shared/contratos/<modulo>/`.
6. SQL versionado por modulo en `sql/`.

## Como agregar un nuevo modulo

1. Crear `modules/<nuevo>/backend/` (paquete Python) con `modulo.py`.
2. Crear `modules/<nuevo>/frontend/` (paquete Dart) con un `ModuloIde`.
3. Registrar el backend en `core/backend/ide_core/config/constants.py`
   (lista `MODULOS_REGISTRADOS`).
4. Registrar el frontend en `apps/ide/lib/nucleo/registro_modulos.dart`.
5. Agregar el contrato JSON en `shared/contratos/<nuevo>/`.
6. Agregar el esquema SQL en `sql/02_schema_<nuevo>.sql`.
7. Si el modulo trae dependencias nuevas, agregarlas a
   `requirements.txt` (RAIZ).

## Equipo GRIS (responsable de la base)

- Ing. Guillermo - Lider tecnico / Core backend
- Ing. Neri - Shell del IDE / Core frontend
- Ing. Erick - QA / DevOps

---

**Ultima actualizacion**: 24 sep. 2026