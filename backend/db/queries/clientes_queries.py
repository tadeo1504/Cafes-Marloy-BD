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

def editar_cliente(conexion, nombre, direccion, telefono, correo):
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
        cursor.execute(consulta, valores)
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
    # Implementar lógica para listar clientes
    pass



if __name__ == "__main__":
    insertar_cliente()
