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
    print("=== Lista de Proveedores ===")
    conexion = crear_conexion()
    if conexion:
        clientes = mostrar_proveedores(conexion)
        cerrar_conexion(conexion)

        if clientes:
            for p in proveedores:
                print(f"ID: {p[0]} | Nombre: {p[1]} | Dirección: {p[2]} | Tel: {p[3]} | Correo: {p[4]}")
        else:
            print("No se encontraron proveedores.")
