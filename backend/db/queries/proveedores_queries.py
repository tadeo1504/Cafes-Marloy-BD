# ABM de proveedores.(insert, update, delete, select)
# Permite manejar el alta, baja, modificacion y consulta de proveedores y luego importarlo en el controlador de proveedores.

from backend.db.conexion import crear_conexion, cerrar_conexion
import mysql.connector

def insertar_proveedor(conexion, nombre, contacto):
    conexion = crear_conexion()
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor()
        consulta = "INSERT INTO proveedores (nombre, contacto) VALUES (%s, %s)"
        cursor.execute(consulta, (nombre, contacto))
        conexion.commit()
        return {"ok": True}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}
    finally:
        cerrar_conexion(conexion)

def editar_proveedor(conexion, id, nombre, contacto):
    conexion = crear_conexion()
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor()
        consulta = """
            UPDATE proveedores
            SET nombre = %s, contacto = %s
            WHERE id = %s
        """
        cursor.execute(consulta, (nombre, contacto, id_proveedor))
        conexion.commit()
        return {"ok": True, "updated": cursor.rowcount}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}
    finally:
        cerrar_conexion(conexion)

def eliminar_proveedor(conexion, id):
    conexion = crear_conexion()
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor()
        consulta = "DELETE FROM proveedores WHERE id = %s"
        cursor.execute(consulta, (id))
        conexion.commit()
        return {"ok": True, "deleted": cursor.rowcount}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}
    finally:
        cerrar_conexion(conexion)

def mostrar_proveedores(conexion):
    conexion = crear_conexion()
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM proveedores")
        resultados = cursor.fetchall()
        return {"ok": True, "data": resultados}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}
    finally:
        cerrar_conexion(conexion)
