# Arquitectura del Monorepo

El producto es el **IDE**. Cada capacidad funcional es un **modulo plug-in**.

## Capas

1. **apps/ide**” Shell Flutter. Layout, navegacion y punto de entrada UI.
   Registra modulos en `nucleo/registro_modulos.dart`.
2. **core/backend**” FastAPI. API gateway que agrega las rutas de todos los
   modulos. Registra modulos en `config/registro_modulos.py`.
3. **core/frontend**” Libreria Dart `ide_core`. Define el contrato
   `ModuloIde`, el `LayoutPrincipal` y los temas.
4. **modules/<nombre>**” Modulo plug-in. Backend: paquete Python con
   `modulo.py` (`registrar(app)`). Frontend: paquete Dart con una clase que
   implementa `ModuloIde`.
5. **shared/contratos**” Contratos JSON entre frontend y backend.
6. **sql/**” Esquema por modulo.

## Flujo de arranque

### Backend (UNICO punto de entrada)

```
cd core/backend
python -m ide_core.main
    -> AppConfig.establecer_conexion()   # crea BD + aplica SQL
    -> AppConfig.iniciar_app()           # arranca uvicorn
         -> crear_app()
              -> configurar_rutas_base()          # /api/v1/salud, /modulos
              -> registrar_modulos(app)           # carga MODULOS_REGISTRADOS
                   -> import herramientas_backend.modulo
                   -> herramientas_backend.modulo.registrar(app)
                        -> app.include_router(router)  # /api/v1/herramientas/*
```

### Frontend (UNICO punto de entrada)

```
cd apps/ide
flutter run -d chrome    # o windows / macos / linux
    -> main()                        # apps/ide/lib/main.dart
    -> construirModulos()            # nucleo/registro_modulos.dart
    -> RegistroModulos([...])
    -> IdeApp -> LayoutPrincipal
```

## Dependencias

TODAS las dependencias del monorepo viven en la RAIZ:

- `requirements.txt`” produccion (core + modulos).
- `requirements-dev.txt`” desarrollo y pruebas.

Un unico `venv/` en la raiz sirve a todo el monorepo.