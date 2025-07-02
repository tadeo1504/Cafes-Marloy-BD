-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS `obligatorio-bd`;
USE `obligatorio-bd`;

-- Tabla login
CREATE TABLE login (
    correo VARCHAR(100) PRIMARY KEY,
    contrasena VARCHAR(255) NOT NULL,
    es_administrador TINYINT(1) DEFAULT 0 CHECK (es_administrador IN (0, 1))
);

-- Tabla proveedores
CREATE TABLE proveedores (
    id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contacto VARCHAR(100)
);

-- Tabla insumos
CREATE TABLE insumos (
    id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255) NOT NULL,
    tipo VARCHAR(50),
    precio_unitario DECIMAL(10,2) NOT NULL,
    id_proveedor SMALLINT,
    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id)
);

-- Tabla clientes
CREATE TABLE clientes (
    id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    correo VARCHAR(100)
);

-- Tabla maquinas
CREATE TABLE maquinas (
    id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(100) NOT NULL,
    id_cliente SMALLINT,
    ubicacion_cliente VARCHAR(255),
    costo_alquiler_mensual DECIMAL(10,2),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);

-- Tabla registro_consumo
CREATE TABLE registro_consumo (
    id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    id_maquina SMALLINT,
    id_insumo SMALLINT,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    cantidad_usada DECIMAL(10,2),
    FOREIGN KEY (id_maquina) REFERENCES maquinas(id),
    FOREIGN KEY (id_insumo) REFERENCES insumos(id)
);

-- Tabla tecnicos
CREATE TABLE tecnicos (
    ci VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(20)
);

-- Tabla mantenimientos
CREATE TABLE mantenimientos (
    id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    id_maquina SMALLINT,
    ci_tecnico VARCHAR(20),
    tipo VARCHAR(100),
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    observaciones TEXT,
    FOREIGN KEY (id_maquina) REFERENCES maquinas(id),
    FOREIGN KEY (ci_tecnico) REFERENCES tecnicos(ci)
);

-- Insertar datos maestros
-- Usuarios login
INSERT INTO login (correo, contrasena, es_administrador) VALUES
('admin1@marloy.com', 'pass', 1),
('admin2@marloy.com', 'pass', 1),
('tecnico1@marloy.com', 'pass', 0),
('cliente1@correo.com', 'pass', 0),
('cliente2@correo.com', 'pass', 0),
('cliente3@correo.com', 'pass', 0),
('cliente4@correo.com', 'pass', 0),
('cliente5@correo.com', 'pass', 0),
('cliente6@correo.com', 'pass', 0),
('cliente7@correo.com', 'pass', 0);

-- Proveedores
INSERT INTO proveedores (id, nombre, contacto) VALUES
(3, 'Distribuidora Central', '098112233'),
(4, 'Proveedora Sur', '094556677'),
(5, 'Insumos del Este', '091234567'),
(6, 'Café Express', '092345678'),
(7, 'TodoMáquinas', '096789012');

-- Insumos
INSERT INTO insumos (id, descripcion, tipo, precio_unitario, id_proveedor) VALUES
(2, 'Café en grano', 'Café', 500.00, 1),
(3, 'Azúcar', 'Edulcorante', 100.00, 2),
(4, 'Vasos descartables', 'Envase', 50.00, 3),
(5, 'Stirrers', 'Accesorio', 30.00, 3),
(6, 'Leche en polvo', 'Lácteo', 120.50, 4),
(7, 'Cacao', 'Chocolate', 150.00, 4),
(8, 'Filtro de café', 'Repuesto', 60.00, 5),
(9, 'Jarra térmica', 'Repuesto', 300.00, 5);

-- Clientes
INSERT INTO clientes (nombre, direccion, telefono, correo) VALUES
('Bar San Juan', '18 de Julio 1234', '099111222', 'sanj@bar.com'),
('Oficina Centenario', 'Rivera 456', '099333444', 'cent@oficina.com'),
('Biblioteca Nacional', 'Colonia 777', '092223344', 'biblio@correo.com'),
('Hospital Central', 'Artigas 999', '098888777', 'hosp@salud.com'),
('Facultad de Ingeniería', 'Gonzalo Ramírez 1450', '094556622', 'fing@uni.com');

-- Máquinas
INSERT INTO maquinas (modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual) VALUES
('ModA1', 1, 'Mostrador', 1500.00),
('ModB2', 1, 'Sala 1', 1400.00),
('ModC3', 2, 'Recepción', 1300.00),
('ModD4', 2, 'Oficina 2', 1600.00),
('ModE5', 3, 'Entrada', 1450.00),
('ModF6', 4, 'Sala espera', 1550.00),
('ModG7', 4, 'Piso 1', 1700.00),
('ModH8', 5, 'Cafetería', 1600.00);

-- Registro de consumo
INSERT INTO registro_consumo (id_maquina, id_insumo, fecha, cantidad_usada) VALUES
(1, 1, '2025-06-01 10:00:00', 3.50),
(1, 2, '2025-06-01 10:00:00', 0.80),
(2, 1, '2025-06-02 11:30:00', 4.00),
(2, 2, '2025-06-02 11:30:00', 1.00),
(3, 1, '2025-06-05 09:45:00', 2.00),
(3, 5, '2025-06-05 09:45:00', 0.60),
(4, 6, '2025-06-07 08:00:00', 1.20),
(5, 1, '2025-06-09 13:10:00', 2.30),
(6, 4, '2025-06-11 14:00:00', 0.50),
(7, 2, '2025-06-13 10:00:00', 1.10),
(8, 1, '2025-06-15 15:00:00', 3.20);

-- Técnicos
INSERT INTO tecnicos (ci, nombre, apellido, telefono) VALUES
('1234567', 'María', 'Lopez', '099123456'),
('2345678', 'José', 'Perez', '098234567'),
('3456789', 'Lucía', 'Fernández', '097345678'),
('4567890', 'Martín', 'Silva', '096456789'),
('5678901', 'Andrés', 'Gómez', '095567890');
