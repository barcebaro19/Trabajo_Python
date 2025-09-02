-- Script para exportar datos de la base de datos persona
-- Ejecuta este script en tu MySQL local para obtener los datos

USE persona;

-- Crear tabla cliente si no existe
CREATE TABLE IF NOT EXISTS cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Apellido VARCHAR(100) NOT NULL,
    Telfono VARCHAR(20),
    email VARCHAR(150)
);

-- Exportar datos existentes (reemplaza con tus datos reales)
-- INSERT INTO cliente (Nombre, Apellido, Telfono, email) VALUES
-- ('Juan', 'Pérez', '123456789', 'juan@test.com'),
-- ('María', 'García', '987654321', 'maria@test.com'),
-- ('Carlos', 'López', '555666777', 'carlos@test.com');

-- Para obtener los datos actuales, ejecuta:
SELECT * FROM cliente;
