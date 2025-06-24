# Maneja altas, bajas, modificaciones y consultas de proveedores.(insert, update, delete y select)
# Solo para administradores.

import mysql.connector
from backend.db.conexion import crear_conexion, cerrar_conexion
from backend.db.queries.proveedores_queries import (
    insertar_proveedor,
    editar_proveedor,
    eliminar_proveedor,
    mostrar_proveedores
)

def alta_proveedor():
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
        exito = editar_proveedor(conexion, id, nombre, direccion, telefono, correo)
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
        exito = eliminar_proveedor(conexion, id)
        cerrar_conexion(conexion)
        if exito:
            print("✅ Proveedor eliminado correctamente.")
        else:
            print("❌ No se pudo eliminar el proveedor.")

def listar_proveedores():
    print("=== Lista de Proveedores ===")
    conexion = crear_conexion()
    if conexion:
        proveedores = mostrar_proveedores(conexion)
        cerrar_conexion(conexion)

        if proveedores:
            for p in proveedores:
                print(f"ID: {p['id']} | Nombre: {p['nombre']} | Dirección: {p['direccion']} | Tel: {p['telefono']} | Correo: {p['correo']}")
        else:
            print("No se encontraron proveedores.")
