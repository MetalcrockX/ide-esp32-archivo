-- Archivo: sql/02_schema_herramientas.sql
-- Esquema del modulo Herramientas (equipo GRIS).

CREATE TABLE IF NOT EXISTS herramientas_dispositivos (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre          TEXT    NOT NULL,
    puerto          TEXT    NOT NULL,
    velocidad       INTEGER NOT NULL DEFAULT 115200,
    placa           TEXT,
    fecha_creacion  TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (puerto)
);

CREATE TABLE IF NOT EXISTS herramientas_historial_flash (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    dispositivo_id  INTEGER NOT NULL,
    archivo         TEXT    NOT NULL,
    exitoso         INTEGER NOT NULL DEFAULT 0,
    salida          TEXT,
    fecha           TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (dispositivo_id)
        REFERENCES herramientas_dispositivos (id) ON DELETE CASCADE
);