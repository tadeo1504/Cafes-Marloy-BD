# Maneja altas, bajas, modificaciones y consultas de proveedores.(insert, update, delete y select)
# Solo para administradores.

import mysql.connector
from backend.db.conexion import crear_conexion, cerrar_conexion


def insertar_proveedor():
    pass

def editar_proveedor():
    pass

def eliminar_proveedor():
    pass

def listar_proveedores():
    # Crear conexión
    conexion = crear_conexion()
    if not conexion:
        print("❌ No se pudo establecer la conexión. Saliendo...")
        return

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM proveedores"
        cursor.execute(consulta)
        proveedores = cursor.fetchall()

        if proveedores:
            print("📋 Lista de Proveedores:")
            for proveedor in proveedores:
                print(proveedor)
        else:
            print("📭 No hay proveedores registrados.")
    except mysql.connector.Error as e:
        print(f"❌ Error al listar proveedores: {e}")
    finally:
        cerrar_conexion(conexion)
