use `obligatorio-bd`;

CREATE TABLE login (
    correo VARCHAR(100) PRIMARY KEY,
    contrasena VARCHAR(255) NOT NULL,
    es_administrador TINYINT(1) DEFAULT 0 CHECK (es_administrador IN (0, 1))
);

CREATE TABLE proveedores (
    id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contacto VARCHAR(100)
);

CREATE TABLE insumos (
    id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255) NOT NULL,
    tipo VARCHAR(50),
    precio_unitario DECIMAL(10,2) NOT NULL,
    id_proveedor SMALLINT,
    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id)
);

CREATE TABLE clientes (
    id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    correo VARCHAR(100)
);

CREATE TABLE maquinas (
    id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(100) NOT NULL,
    id_cliente SMALLINT,
    ubicacion_cliente VARCHAR(255),
    costo_alquiler_mensual DECIMAL(10,2),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);

CREATE TABLE registro_consumo (
    id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    id_maquina SMALLINT,
    id_insumo SMALLINT,
    fecha DATE,
    cantidad_usada DECIMAL(10,2),
    FOREIGN KEY (id_maquina) REFERENCES maquinas(id),
    FOREIGN KEY (id_insumo) REFERENCES insumos(id)
);

CREATE TABLE tecnicos (
    ci VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(20)
);

CREATE TABLE mantenimientos (
    id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    id_maquina SMALLINT,
    ci_tecnico VARCHAR(20),
    tipo VARCHAR(100),
    fecha DATE,
    observaciones TEXT,
    FOREIGN KEY (id_maquina) REFERENCES maquinas(id),
    FOREIGN KEY (ci_tecnico) REFERENCES tecnicos(ci)
);