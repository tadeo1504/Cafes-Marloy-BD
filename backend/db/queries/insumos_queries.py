# ABM de insumos.(insert, update, delete, select)
# Permite manejar el alta, baja, modificacion y consulta de insumos y luego importarlo en el controlador de insumos.

from backend.db.conexion import crear_conexion, cerrar_conexion
import mysql.connector

def insertar_insumos(conexion, nombre, direccion, telefono, correo):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return

    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            INSERT INTO insumos (nombre, direccion, telefono, correo)
            VALUES (%s, %s, %s, %s)
        """
        valores = (nombre, direccion, telefono, correo)
        cursor.execute(consulta, valores)
        conexion.commit()
        print("✅ Cliente insertado exitosamente.")
    except mysql.connector.Error as e:
        print(f"❌ Error al insertar insumos: {e}")
    finally:
        cerrar_conexion(conexion)

def editar_insumos(conexion, nombre, direccion, telefono, correo, id_cliente):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return
    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            UPDATE insumos
            SET nombre = %s, direccion = %s, telefono = %s, correo = %s
            WHERE id_insumo = %s
        """
        valores = (nombre, direccion, telefono, correo, id_cliente)
        cursor.execute(consulta, valores)
        conexion.commit()
        if cursor.rowcount > 0:
            print("✅ Insumos editado exitosamente.")
        else:
            print("📭 No se encontraron insumos con ese ID.")
    except mysql.connector.Error as e:
        print(f"❌ Error al editar insumos: {e}")
    finally:
        cerrar_conexion(conexion)
        

def eliminar_insumos(conexion, id):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return
    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            DELETE insumos
            WHERE id_insumo = %s
        """
        cursor.execute(consulta, id)
        conexion.commit()
        if cursor.rowcount > 0:
            print("✅ Insumo eliminado exitosamente.")
        else:
            print("📭 No se encontraron insumos con ese ID.")
    except mysql.connector.Error as e:
        print(f"❌ Error al eliminar insumos: {e}")
    finally:
        cerrar_conexion(conexion)
        
def listar_insumos(conexion):
    conexion = crear_conexion()
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM insumos")
        resultados = cursor.fetchall()
        return {"ok": True, "data": resultados}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}
    finally:
        cerrar_conexion(conexion)
