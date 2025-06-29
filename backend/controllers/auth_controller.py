#para checkear el login de un usuario
import mysql.connector
from backend.db.conexion import crear_conexion, cerrar_conexion
import hashlib

import jwt
import datetime
from backend.db.conexion import crear_conexion, cerrar_conexion
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

def login_usuario(correo, contrasena):
    conexion = crear_conexion()
    if not conexion:
        return {"success": False, "error": "No se pudo conectar a la base de datos"}

    try:
        # Hash de la contraseña
        hashed_contrasena = hashlib.sha256(contrasena.encode()).hexdigest()

        # Verificar las credenciales
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM login WHERE correo = %s AND contrasena = %s", (correo, hashed_contrasena))
        usuario = cursor.fetchone()

        if usuario:
            payload = {
                "correo": correo,
                "es_administrador": usuario["es_administrador"],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=3)
            }

            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

            return {
                "success": True,
                "usuario": {
                    "correo": usuario["correo"],
                    "es_administrador": bool(usuario["es_administrador"])
                },
                "token": token
            }


        return {"success": False, "error": "Credenciales incorrectas"}

    except Exception as e:
        return {"success": False, "error": str(e)}

    finally:
        cerrar_conexion(conexion)


def registrar_usuario(correo, contrasena):
    conexion = crear_conexion()
    if conexion is None:
        return {'error': 'No se pudo conectar a la base de datos.'}
    else:
        try:
            cursor = conexion.cursor()
            hashed_contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
            query = 'INSERT INTO login (correo, contrasena) VALUES (%s, %s)'
            cursor.execute(query, (correo, hashed_contrasena))
            conexion.commit()
            return {'success': True, 'message': 'Usuario registrado exitosamente.'}
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_DUP_ENTRY:
                return {'error': 'El correo ya está registrado.'}
            else:
                return {'error': f'Error al registrar el usuario: {err}'}
        finally:
            cerrar_conexion(conexion)



            
