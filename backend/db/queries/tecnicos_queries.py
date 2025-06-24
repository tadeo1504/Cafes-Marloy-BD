# ABM de tecnicos.(insert, update, delete, select)
# Permite manejar el alta, baja, modificacion y consulta de tecnicos y luego importarlo en el controlador de tecnicos.

from backend.db.conexion import crear_conexion, cerrar_conexion
import mysql.connector

def insertar_tecnico(conexion, ci, nombre, apellido, telefono):
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor()
        consulta = '''INSERT INTO tecnicos (ci, nombre, apellido, telefono) VALUES (%s, %s, %s, %s)'''
        cursor.execute(consulta, (ci, nombre, apellido, telefono))
        conexion.commit()
        return {"ok": True}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}
    finally:
        cerrar_conexion(conexion)

def editar_tecnico(conexion, ci, nombre, apellido, telefono):
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor()
        consulta = """
            UPDATE tecnicos
            SET ci = %s, nombre = %s, apellido = %s, telefono = %s
            WHERE ci = %s
        """
        cursor.execute(consulta, (ci, nombre, apellido, telefono))
        conexion.commit()
        return {"ok": True, "updated": cursor.rowcount}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}
    finally:
        cerrar_conexion(conexion)

def eliminar_tecnico(conexion, ci):
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor()
        consulta = "DELETE FROM tecnicos WHERE ci = %s"
        cursor.execute(consulta, (ci))
        conexion.commit()
        return {"ok": True, "deleted": cursor.rowcount}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}
    finally:
        cerrar_conexion(conexion)

def mostrar_tecnicos(conexion):
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tecnicos")
        resultados = cursor.fetchall()
        return {"ok": True, "data": resultados}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}
    finally:
        cerrar_conexion(conexion)
