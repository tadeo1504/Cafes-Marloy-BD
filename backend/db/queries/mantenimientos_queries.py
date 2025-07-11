# ABM de mantenimientos.(insert, update, delete, select)
# Permite manejar el alta, baja, modificacion y consulta de mantenimientos y luego importarlo en el controlador de mantenimientos.

import mysql.connector

def insertar_mantenimiento(conexion, id_maquina, ci_tecnico, tipo, observaciones):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return

    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            INSERT INTO mantenimientos (id_maquina, ci_tecnico, tipo, observaciones)
            VALUES (%s, %s, %s, %s)
        """
        valores = (id_maquina, ci_tecnico, tipo, observaciones)
        cursor.execute(consulta, valores)
        conexion.commit()
        return True
    except mysql.connector.Error as e:
        print(f"❌ Error al insertar mantenimiento: {e}")


def editar_mantenimiento(conexion, id_maquina, ci_tecnico, tipo, fecha, observaciones, id):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return
    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            UPDATE mantenimientos
            SET id_maquina = %s, ci_tecnico = %s, tipo = %s, fecha = %s, observaciones = %s
            WHERE id = %s
        """
        valores = (id_maquina, ci_tecnico, tipo, fecha, observaciones, id)
        cursor.execute(consulta, valores)
        conexion.commit()
        if cursor.rowcount > 0:
            return True
        else:
            print("📭 No se encontró un mantenimiento con ese ID.")
    except mysql.connector.Error as e:
        print(f"❌ Error al editar mantenimiento: {e}")

        

def eliminar_mantenimiento(conexion, id):
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return
    # Armar y ejecutar consulta
    try:
        cursor = conexion.cursor()
        consulta = """
            DELETE mantenimientos
            WHERE id = %s
        """
        cursor.execute(consulta, (id,))  
        conexion.commit()
        if cursor.rowcount > 0:
            print("✅ Mantenimiento eliminado exitosamente.")
        else:
            print("📭 No se encontró un mantenimiento con ese ID.")
    except mysql.connector.Error as e:
        print(f"❌ Error al eliminar mantenimiento: {e}")

        
def mostrar_mantenimientos(conexion):
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM mantenimientos")
        resultados = cursor.fetchall()
        return {"ok": True, "data": resultados}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}

