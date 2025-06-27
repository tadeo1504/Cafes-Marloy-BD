# ABM de insumos.(insert, update, delete, select)
# Permite manejar el alta, baja, modificacion y consulta de insumos y luego importarlo en el controlador de insumos.

from backend.db.conexion import crear_conexion, cerrar_conexion
import mysql.connector

def insertar_insumo(conexion, descripcion, tipo, precio_unitario, id_proveedor):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return

    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            INSERT INTO insumos (descripcion, tipo, precio_unitario, id_proveedor)
            VALUES (%s, %s, %s, %s)
        """
        valores = (descripcion, tipo, precio_unitario, id_proveedor)
        cursor.execute(consulta, valores)
        conexion.commit()
        return True
    except mysql.connector.Error as e:
        print(f"❌ Error al insertar insumos: {e}")
    finally:
        cerrar_conexion(conexion)

def editar_insumo(conexion, descripcion, tipo, precio_unitario, id_proveedor):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return
    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            UPDATE insumos
            SET descripcion = %s, tipo = %s, precio_unitario = %s, id_proveedor = %s
            WHERE id = %s
        """
        valores = (descripcion, tipo, precio_unitario, id_proveedor)
        cursor.execute(consulta, valores)
        conexion.commit()
        if cursor.rowcount > 0:
            print("✅ Insumo editado exitosamente.")
        else:
            print("📭 No se encontraron insumos con ese ID.")
    except mysql.connector.Error as e:
        print(f"❌ Error al editar insumos: {e}")
    finally:
        cerrar_conexion(conexion)
        

def eliminar_insumo(conexion, id):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return
    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            DELETE insumos
            WHERE id = %s
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
        
def mostrar_insumos(conexion):
    conexion = crear_conexion()
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM insumos")
        resultados = cursor.fetchall()
        if not resultados:
            return {"ok": False, "error": "No se encontraron insumos."}
        
        return {"ok": True, "data": resultados}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}
    finally:
        cerrar_conexion(conexion)
