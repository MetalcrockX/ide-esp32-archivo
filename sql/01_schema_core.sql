-- Archivo: sql/01_schema_core.sql
-- Esquema base del IDE (compartido por todos los modulos).

CREATE TABLE IF NOT EXISTS usuarios (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario         TEXT    NOT NULL UNIQUE,
    password_hash   TEXT    NOT NULL,
    rol             TEXT    NOT NULL DEFAULT 'operador',
    activo          INTEGER NOT NULL DEFAULT 1,
    fecha_creacion  TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS modulos_instalados (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre          TEXT    NOT NULL UNIQUE,
    version         TEXT    NOT NULL,
    activo          INTEGER NOT NULL DEFAULT 1,
    fecha_alta      TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP
);