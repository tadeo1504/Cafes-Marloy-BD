# Maneja altas, bajas, modificaciones y consultas de proveedores.(insert, update, delete y select)
# Solo para administradores.

import mysql.connector
from backend.db.conexion import crear_conexion, cerrar_conexion
from backend.db.queries.proveedores_queries import (
    insertar_proveedores,
    editar_proveedores,
    eliminar_proveedores,
    mostrar_proveedores
)

def insertar_proveedor():
    print("=== Insertar Proveedor ===")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")

    conexion = crear_conexion()
    if conexion:
        exito = insertar_proveedor(conexion, nombre, direccion, telefono, correo)
        cerrar_conexion(conexion)
        if exito:
            print("✅ Proveedor insertado correctamente.")
        else:
            print("❌ No se pudo insertar el proveedor.")

def modificar_proveedor():
    print("=== Modificación de Proveedor ===")
    id = input("ID del Proveedor a modificar: ")
    nombre = input("Nuevo Nombre: ")
    direccion = input("Nueva Dirección: ")
    telefono = input("Nuevo Teléfono: ")
    correo = input("Nuevo Correo: ")

    conexion = crear_conexion()
    if conexion:
        exito = editar_cliente(conexion, nombre, direccion, telefono, correo, id)
        cerrar_conexion(conexion)
        if exito:
            print("✅ Cliente modificado correctamente.")
        else:
            print("❌ No se pudo modificar el cliente.")

def baja_proveedor():
    print("=== Baja de Proveedor ===")
    id = input("ID del Proveedor a eliminar: ")

    conexion = crear_conexion()
    if conexion:
        exito = eliminar_cliente(conexion, id)
        cerrar_conexion(conexion)
        if exito:
            print("✅ Proveedor eliminado correctamente.")
        else:
            print("❌ No se pudo eliminar el proveedor.")

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
