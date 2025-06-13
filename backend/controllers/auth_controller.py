#para checkear el login de un usuario
import mysql.connector
from backend.db.conexion import crear_conexion, cerrar_conexion
import hashlib

def login_usuario(correo, contrasena):
    conexion = crear_conexion()
    if conexion is None:
        return {'error': 'No se pudo conectar a la base de datos.'}
    else:
        try:
            #dictionary true para que el cursor devuelva un diccionario
            cursor = conexion.cursor(dictionary=True)
            hashed_contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
            query = 'SELECT * FROM login WHERE correo = %s AND contrasena = %s'
            cursor.execute(query, (correo, hashed_contrasena))
            usuario = cursor.fetchone()
            if usuario:
                token = hashlib.sha256((correo + contrasena).encode()).hexdigest()
                return {'success': True, 'usuario': usuario, 'token': token}
            else:
                return {'error': 'Usuario o contraseña incorrectos.'}
        except mysql.connector.Error as err:
            return {'error': f'Error al consultar la base de datos: {err}'}
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
            return {'error': f'Error al registrar el usuario: {err}'}
        finally:
            cerrar_conexion(conexion)

            
