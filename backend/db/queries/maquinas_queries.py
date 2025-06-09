# ABM de maquinas.(insert, update, delete, select)
# Permite manejar el alta, baja, modificacion y consulta de maquinas y luego importarlo en el controlador de maquinas.

from backend.db.conexion import crear_conexion, cerrar_conexion
import mysql.connector

def insertar_maquina(conexion, nombre, direccion, telefono, correo):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return

    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            INSERT INTO maquinas (nombre, direccion, telefono, correo)
            VALUES (%s, %s, %s, %s)
        """
        valores = (nombre, direccion, telefono, correo)
        cursor.execute(consulta, valores)
        conexion.commit()
        print("✅ Maquina insertada exitosamente.")
    except mysql.connector.Error as e:
        print(f"❌ Error al insertar maquina: {e}")
    finally:
        cerrar_conexion(conexion)

def editar_maquina(conexion, nombre, direccion, telefono, correo, id_maquina):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return
    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            UPDATE maquinas
            SET nombre = %s, direccion = %s, telefono = %s, correo = %s
            WHERE id_maquina = %s
        """
        valores = (nombre, direccion, telefono, correo, id_maquina)
        cursor.execute(consulta, valores)
        conexion.commit()
        if cursor.rowcount > 0:
            print("✅ Maquina editada exitosamente.")
        else:
            print("📭 No se encontró una maquina con ese ID.")
    except mysql.connector.Error as e:
        print(f"❌ Error al editar maquina: {e}")
    finally:
        cerrar_conexion(conexion)
        

def eliminar_maquina(conexion, id):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return
    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            DELETE maquinas
            WHERE id_maquina = %s
        """
        cursor.execute(consulta, id)
        conexion.commit()
        if cursor.rowcount > 0:
            print("✅ Maquina eliminada exitosamente.")
        else:
            print("📭 No se encontró una maquina con ese ID.")
    except mysql.connector.Error as e:
        print(f"❌ Error al eliminar maquina: {e}")
    finally:
        cerrar_conexion(conexion)
        
def listar_maquinas(conexion):
    conexion = crear_conexion()
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM maquinas")
        resultados = cursor.fetchall()
        return {"ok": True, "data": resultados}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}
    finally:
        cerrar_conexion(conexion)
