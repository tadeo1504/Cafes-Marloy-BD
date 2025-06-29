# ABM de proveedores.(insert, update, delete, select)
# Permite manejar el alta, baja, modificacion y consulta de proveedores y luego importarlo en el controlador de proveedores.

import mysql.connector

def insertar_proveedor(conexion, nombre, contacto):
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


def editar_proveedor(conexion, id, nombre, contacto):
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor()
        consulta = """
            UPDATE proveedores
            SET nombre = %s, contacto = %s
            WHERE id = %s
        """
        cursor.execute(consulta, (nombre, contacto, id))
        conexion.commit()
        return {"ok": True, "updated": cursor.rowcount}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}


def eliminar_proveedor(conexion, id):
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor()
        consulta = "DELETE FROM proveedores WHERE id = %s"
        cursor.execute(consulta, (id,))  
        conexion.commit()
        if cursor.rowcount == 0:
            return {"ok": False, "error": "No se encontró el proveedor con ese ID"}
        return {"ok": True, "deleted": cursor.rowcount}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}


def mostrar_proveedores(conexion):
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM proveedores")
        resultados = cursor.fetchall()
        return {"ok": True, "data": resultados}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}

