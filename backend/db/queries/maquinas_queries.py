# ABM de maquinas.(insert, update, delete, select)
# Permite manejar el alta, baja, modificacion y consulta de maquinas y luego importarlo en el controlador de maquinas.

from backend.db.conexion import crear_conexion, cerrar_conexion
import mysql.connector

def insertar_maquina(conexion, modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return

    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            INSERT INTO maquinas (modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual)
            VALUES (%s, %s, %s, %s)
        """
        valores = (modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual)
        cursor.execute(consulta, valores)
        conexion.commit()
        print("✅ Maquina insertada exitosamente.")
    except mysql.connector.Error as e:
        print(f"❌ Error al insertar maquina: {e}")
    finally:
        cerrar_conexion(conexion)

def editar_maquina(conexion, modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return
    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            UPDATE maquinas
            SET modelo = %s, id_cliente = %s, ubicacion_cliente = %s, costo_alquiler_mensual = %s
            WHERE id = %s
        """
        valores = (modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual)
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
            WHERE id = %s
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
