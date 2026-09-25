-- Archivo: sql/03_triggers.sql

CREATE TRIGGER IF NOT EXISTS trg_modulos_actualizado
AFTER UPDATE ON modulos_instalados
BEGIN
    UPDATE modulos_instalados
    SET fecha_alta = fecha_alta
    WHERE id = NEW.id;
END;