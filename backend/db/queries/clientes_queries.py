#ABM de clientes.
# para manejar el alta, baja, modificacion y consulta de clientes
# es decir insert, update, delete y select
# y luego importarlo en el controlador de clientes.

from backend.db.conexion import crear_conexion, cerrar_conexion
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
        print("✅ Cliente insertado exitosamente.")
    except mysql.connector.Error as e:
        print(f"❌ Error al insertar cliente: {e}")
    finally:
        cerrar_conexion(conexion)

def editar_cliente(conexion, nombre, direccion, telefono, correo, id_cliente):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return
    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            UPDATE clientes
            SET nombre = %s, direccion = %s, telefono = %s, correo = %s
            WHERE id_cliente = %s
        """
        valores = (nombre, direccion, telefono, correo, id_cliente)
        cursor.execute(consulta, valores)
        conexion.commit()
        if cursor.rowcount > 0:
            print("✅ Cliente editado exitosamente.")
        else:
            print("📭 No se encontró un cliente con ese ID.")
    except mysql.connector.Error as e:
        print(f"❌ Error al editar cliente: {e}")
    finally:
        cerrar_conexion(conexion)
        

def eliminar_cliente(conexion, id):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return
    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            DELETE clientes
            WHERE id_cliente = %s
        """
        cursor.execute(consulta, id)
        conexion.commit()
        if cursor.rowcount > 0:
            print("✅ Cliente eliminado exitosamente.")
        else:
            print("📭 No se encontró un cliente con ese ID.")
    except mysql.connector.Error as e:
        print(f"❌ Error al eliminar cliente: {e}")
    finally:
        cerrar_conexion(conexion)
        
def listar_clientes(conexion):
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT id, nombre, direccion, telefono, correo FROM clientes")
        clientes = cursor.fetchall()
        
        if not clientes:
            print("No hay clientes registrados.")
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

