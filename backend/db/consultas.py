from backend.db.conexion import crear_conexion, ejecutar_consulta, cerrar_conexion

conexion = crear_conexion()

if conexion:
    consulta = """SELECT * FROM clientes"""
    try:
        cursor = conexion.cursor()
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)
    except Exception as e:
        print(f"❌ Error al ejecutar la consulta: {e}")
    finally:
        cerrar_conexion(conexion)
        
