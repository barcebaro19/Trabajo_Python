-- Script SQL para crear la base de datos y tabla cliente
-- Ejecuta este script en MySQL Workbench o en la línea de comandos de MySQL

-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS persona;

-- Usar la base de datos
USE persona;

-- Crear la tabla cliente si no existe
CREATE TABLE IF NOT EXISTS cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Insertar algunos datos de ejemplo
INSERT INTO cliente (nombre, apellido, telefono, email) VALUES
('Juan', 'Pérez', '123456789', 'juan.perez@email.com'),
('María', 'García', '987654321', 'maria.garcia@email.com'),
('Carlos', 'López', '555123456', 'carlos.lopez@email.com'),
('Ana', 'Martínez', '777888999', 'ana.martinez@email.com'),
('Luis', 'Rodríguez', '111222333', 'luis.rodriguez@email.com');

-- Verificar que la tabla se creó correctamente
DESCRIBE cliente;

-- Mostrar los datos insertados
SELECT * FROM cliente;
