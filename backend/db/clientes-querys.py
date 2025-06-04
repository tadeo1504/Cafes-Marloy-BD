#abm de clientes
# para manejar el alta, baja, modificacion y consulta de clientes
# es decir insert, update, delete y select
# y luego importarlo en el controlador de clientes

from backend.db.conexion import crear_conexion, cerrar_conexion
import mysql.connector

def insertar_cliente():
    # Pedir datos al usuario
    nombre = input("📥 Ingresá el nombre del cliente: ").strip()
    direccion = input("📥 Ingresá la dirección: ").strip()
    telefono = input("📥 Ingresá el teléfono: ").strip()
    correo = input("📥 Ingresá el correo: ").strip()

    # Crear conexión
    conexion = crear_conexion()
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

def editar_cliente():
    #pedir ID del cliente a editar
    id_cliente = input("📥 Ingresá el ID del cliente a editar: ").strip()
    # Pedir nuevos datos al usuario
    nombre = input("📥 Ingresá el nuevo nombre del cliente: ").strip()
    direccion = input("📥 Ingresá la nueva dirección: ").strip()
    telefono = input("📥 Ingresá el nuevo teléfono: ").strip()
    correo = input("📥 Ingresá el nuevo correo: ").strip()
    # Crear conexión
    conexion = crear_conexion()
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
        

def eliminar_cliente():
    # Implementar lógica para eliminar cliente
    pass

def listar_clientes():
    # Implementar lógica para listar clientes
    pass



if __name__ == "__main__":
    insertar_cliente()
