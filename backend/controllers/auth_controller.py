#para checkear el login de un usuario
import mysql.connector
from backend.database.db import crear_conexion, cerrar_conexion
import hashlib

def login_usuario(username, password):
    conexion = crear_conexion()
    if conexion is None:
        return {'error': 'No se pudo conectar a la base de datos.'}
    else:
        try:
            #dictionary true para que el cursor devuelva un diccionario
            cursor = conexion.cursor(dictionary=True)
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            query = 'SELECT * FROM login WHERE username = %s AND password = %s'
            cursor.execute(query, (username, hashed_password))
            usuario = cursor.fetchone()
            if usuario:
                return {'success': True, 'usuario': usuario}
            else:
                return {'error': 'Usuario o contraseña incorrectos.'}
        except mysql.connector.Error as err:
            return {'error': f'Error al consultar la base de datos: {err}'}
        finally:
            cerrar_conexion(conexion)

def registrar_usuario(username, password):
    conexion = crear_conexion()
    if conexion is None:
        return {'error': 'No se pudo conectar a la base de datos.'}
    else:
        try:
            cursor = conexion.cursor()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            query = 'INSERT INTO login (username, password) VALUES (%s, %s)'
            cursor.execute(query, (username, hashed_password))
            conexion.commit()
            return {'success': True, 'message': 'Usuario registrado exitosamente.'}
        except mysql.connector.Error as err:
            return {'error': f'Error al registrar el usuario: {err}'}
        finally:
            cerrar_conexion(conexion)

            
