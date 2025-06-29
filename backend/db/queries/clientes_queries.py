# ABM de clientes.(insert, update, delete, select)
# Permite manejar el alta, baja, modificacion y consulta de clientes y luego importarlo en el controlador de clientes.

import mysql.connector

def insertar_cliente(conexion, nombre, direccion, telefono, correo):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return

    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            INSERT INTO clientes (nombre, direccion, telefono, correo)
            VALUES (%s, %s, %s, %s)
        """
        valores = (nombre, direccion, telefono, correo)
        cursor.execute(consulta, valores)
        conexion.commit()
        return True
    except mysql.connector.Error as e:
        return False
    

def editar_cliente(conexion, nombre, direccion, telefono, correo, id):
    if not conexion:
        return False
    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            UPDATE clientes
            SET nombre = %s, direccion = %s, telefono = %s, correo = %s
            WHERE id = %s
        """
        valores = (nombre, direccion, telefono, correo, id)
        cursor.execute(consulta, valores)
        conexion.commit()
        if cursor.rowcount > 0:
            return True
        else:
            print("📭 No se encontraron clientes con ese ID.")
            return False
    except mysql.connector.Error as e:
        return False
            

def eliminar_cliente(conexion, id):
    if not conexion:
        return False
    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            DELETE FROM clientes
            WHERE id = %s
        """
        cursor.execute(consulta, (int(id),))  
        conexion.commit()
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except mysql.connector.Error as e:
        print("Error al eliminar cliente:", e)
        return False

        
def mostrar_clientes(conexion):
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        
        if not clientes:
            print("No hay clientes registrados.")
            return []

        else:
            return {"ok": True, "data": clientes}

    except Exception as e:
        print("Error al listar clientes:", e)

