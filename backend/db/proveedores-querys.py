#ABM de proveedores
# para manejar el alta, baja, modificacion y consulta de proveedores
# es decir insert, update, delete y select
# y luego importarlo en el controlador de proveedores

from backend.db.conexion import crear_conexion, cerrar_conexion
import mysql.connector

def insertar_proveedor():
    # Pedir datos al usuario
    nombre = input("📥 Ingresá el nombre del proveedor: ").strip()
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
            INSERT INTO proveedores (nombre, direccion, telefono, correo)
            VALUES (%s, %s, %s, %s)
        """
        valores = (nombre, direccion, telefono, correo)
        cursor.execute(consulta, valores)
        conexion.commit()
        print("✅ Proveedor insertado exitosamente.")
    except mysql.connector.Error as e:
        print(f"❌ Error al insertar proveedor: {e}")
    finally:
        cerrar_conexion(conexion)

def editar_proveedor():
    #pedir ID del proveedor a editar
    id_proveedor = input("📥 Ingresá el ID del proveedor a editar: ").strip()
    # Pedir nuevos datos al usuario
    nombre = input("📥 Ingresá el nuevo nombre del proveedor: ").strip()
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
            UPDATE proveedores
            SET nombre = %s, direccion = %s, telefono = %s, correo = %s
            WHERE id_proveedor = %s
        """
        valores = (nombre, direccion, telefono, correo, id_proveedores)
        cursor.execute(consulta, valores)
        conexion.commit()
        if cursor.rowcount > 0:
            print("✅ Proveedor editado exitosamente.")
        else:
            print("📭 No se encontró un proveedor con ese ID.")
    except mysql.connector.Error as e:
        print(f"❌ Error al editar proveedor: {e}")
    finally:
        cerrar_conexion(conexion)
        

def eliminar_proveedor():
    # Implementar lógica para eliminar proveedores
    pass

def listar_proveedor():
    # Implementar lógica para listar proveedores
    pass



if __name__ == "__main__":
    insertar_proveedor()
