<h1 align="center">Cafés Marloy <br>UCU</h1>

###

<div align="left">
  <img src="https://s3.us-east-1.wasabisys.com/imasd/2022/10/Logo-UCU-001-FINAL-03_ID_Uruguay.jpg" width="51" height="29" alt="UCU logo" />
</div>


###

<p align="left">Esto es un sistema para la UCU, donde se implementará un sistema administrativo para gestionar sus máquinas expendedoras de café.</p>

###

<h2 align="left">Materia Base de Datos 1</h2>

###

<p align="left">✨ Entrega Obligatoria de la Materia<br>📚 Hecho por los Estudiantes :<br><br>Joaquin Hernandez<br>Tadeo Rodriguez<br>☕🤎🥯🍪</p>

###

## Instrucciones de Instalación y Ejecución

### Prerrequisitos

- Python 3.11 o superior
- MySQL 
- Node.js y npm

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tadeo1504/Cafes-Marloy-BD
cd Cafes-Marloy-BD
```

### 2. Configurar el Backend

#### Instalar dependencias de Python

```bash
pip install flask flask-cors mysql-connector-python mysqlclient PyJWT python-dotenv
```

#### Configurar variables de entorno

Crear un archivo `.env` en la carpeta `backend/` con la siguiente configuración:

```properties
DB_HOST=localhost
DB_NAME=obligatorio-bd
SECRET_KEY=a_secret_key

DB_ADMIN_USER=admin_user
DB_ADMIN_PASSWORD=admin123

DB_USER_COMUN=usuario_comun
DB_PASSWORD_COMUN=comun123
```

**Importante:** Modifica los valores de `DB_ADMIN_USER`, `DB_ADMIN_PASSWORD`, `DB_USER_COMUN` y `DB_PASSWORD_COMUN` según las credenciales de tu servidor MySQL local.

#### Configurar la base de datos

**Primera vez solamente:** Configurar credenciales de MySQL en `backend/db/crear_db.py` y ejecutar:

```bash
python -m backend.db.crear_db
```

Este comando creará las tablas, usuarios y datos iniciales.

### 3. Configurar el Frontend

Navegar a la carpeta del frontend:

```bash
cd frontend-marloy
npm install
```

### 4. Ejecutar la Aplicación

#### Opción A: Backend interactivo (solo consola)

Desde la raíz del proyecto:

```bash
python -m backend.app_backend
```

#### Opción B: Aplicación completa (Backend + Frontend)

**Terminal 1 - Backend:**
Desde la raíz del proyecto:

```bash
python -m backend.app
```

**Terminal 2 - Frontend:**
Desde la carpeta `frontend-marloy`:

```bash
cd frontend-marloy
npm run dev
```

Una vez ejecutados ambos comandos, la aplicación estará disponible en la URL que indique Vite (generalmente `http://localhost:5173`).

###
