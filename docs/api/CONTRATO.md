# Contratos API

Cada componente del IDE versiona su contrato por separado:

| Componente | Ubicacion | Prefijo |
|------------|-----------|---------|
| Core IDE | `shared/contratos/core/api_v1.json` | `/api/v1` |
| Modulo Herramientas | `shared/contratos/herramientas/api_v1.json` | `/api/v1/herramientas` |

Un cambio incompatible requiere version `v2` y actualizacion del contrato.