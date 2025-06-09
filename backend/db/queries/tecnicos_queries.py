# ABM de tecnicos.(insert, update, delete, select)
# Permite manejar el alta, baja, modificacion y consulta de tecnicos y luego importarlo en el controlador de tecnicos.

from backend.db.conexion import crear_conexion, cerrar_conexion
import mysql.connector

def insertar_tecnico(nombre, contacto):
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

def editar_tecnico(id_tecnico, nombre, contacto):
    conexion = crear_conexion()
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor()
        consulta = """
            UPDATE tecnicos
            SET nombre = %s, contacto = %s
            WHERE id_tecnico = %s
        """
        cursor.execute(consulta, (nombre, contacto, id_tecnico))
        conexion.commit()
        return {"ok": True, "updated": cursor.rowcount}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}
    finally:
        cerrar_conexion(conexion)

def eliminar_tecnico(id_tecnico):
    conexion = crear_conexion()
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor()
        consulta = "DELETE FROM tecnicos WHERE id_tecnico = %s"
        cursor.execute(consulta, (id_proveedor,))
        conexion.commit()
        return {"ok": True, "deleted": cursor.rowcount}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}
    finally:
        cerrar_conexion(conexion)

def listar_tecnicos():
    conexion = crear_conexion()
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
