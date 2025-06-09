# ABM de mantenimientos.(insert, update, delete, select)
# Permite manejar el alta, baja, modificacion y consulta de clientes y luego importarlo en el controlador de clientes.

from backend.db.conexion import crear_conexion, cerrar_conexion
import mysql.connector

def insertar_mantenimientos(conexion, nombre, direccion, telefono, correo):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return

    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            INSERT INTO mantenimientos (nombre, direccion, telefono, correo)
            VALUES (%s, %s, %s, %s)
        """
        valores = (nombre, direccion, telefono, correo)
        cursor.execute(consulta, valores)
        conexion.commit()
        print("✅ Mantenimiento insertado exitosamente.")
    except mysql.connector.Error as e:
        print(f"❌ Error al insertar mantenimiento: {e}")
    finally:
        cerrar_conexion(conexion)

def editar_mantenimiento(conexion, nombre, direccion, telefono, correo, id_cliente):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return
    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            UPDATE mantenimientos
            SET nombre = %s, direccion = %s, telefono = %s, correo = %s
            WHERE id_cliente = %s
        """
        valores = (nombre, direccion, telefono, correo, id_cliente)
        cursor.execute(consulta, valores)
        conexion.commit()
        if cursor.rowcount > 0:
            print("✅ Mantenimiento editado exitosamente.")
        else:
            print("📭 No se encontró un mantenimiento con ese ID.")
    except mysql.connector.Error as e:
        print(f"❌ Error al editar mantenimiento: {e}")
    finally:
        cerrar_conexion(conexion)
        

def eliminar_mantenimiento(conexion, id):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return
    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            DELETE mantenimientos
            WHERE id_mantenimiento = %s
        """
        cursor.execute(consulta, id)
        conexion.commit()
        if cursor.rowcount > 0:
            print("✅ Mantenimiento eliminado exitosamente.")
        else:
            print("📭 No se encontró un mantenimiento con ese ID.")
    except mysql.connector.Error as e:
        print(f"❌ Error al eliminar mantenimiento: {e}")
    finally:
        cerrar_conexion(conexion)
        
def listar_mantenimiento(conexion):
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT id, nombre, direccion, telefono, correo FROM mantenimientos")
        clientes = cursor.fetchall()
        
        if not mantenimientos:
            print("No hay mantenimientos registrados.")
            return
        
        print("\n=== Lista de Clientes ===")
        for cliente in clientes:
            id, nombre, direccion, telefono, correo = cliente
            print(f"ID: {id}")
            print(f"Nombre: {nombre}")
            print(f"Dirección: {direccion}")
            print(f"Teléfono: {telefono}")
            print(f"Correo: {correo}")
    
    except Exception as e:
        print("Error al listar clientes:", e)
    
    finally:
        cursor.close()
