#Maneja altas, bajas, modificaciones y consultas de insumos.(insert, update, delete y select)

import mysql.connector
from backend.db.conexion import crear_conexion, cerrar_conexion
from backend.db.queries.insumos_queries import (
    insertar_insumos,
    editar_insumos,
    eliminar_insumos,
    mostrar_insumos
)

def alta_insumo():
    print("=== Alta de Insumo ===")
    descripcion = input("Descripción: ")
    tipo = input("Tipo: ")
    precio_unitario = input("Precio unitario: ")
    id = input("Id del Proveedor: ")

    conexion = crear_conexion()
    if conexion:
        exito = insertar_insumo(conexion, descripcion, tipo, precio_unitario, id)
        cerrar_conexion(conexion)
        if exito:
            print("Insumo insertado correctamente.")
        else:
            print("No se pudo insertar el insumo.")
    
    
def modificar_insumo():
    print("=== Modificación de Insumo ===")
    id = input("ID del Insumo a modificar: ")
    nombre = input("Nuevo Nombre: ")
    direccion = input("Nueva Dirección: ")
    telefono = input("Nuevo Teléfono: ")
    correo = input("Nuevo Correo: ")

    conexion = crear_conexion()
    if conexion:
        exito = editar_insumo(conexion, nombre, direccion, telefono, correo, id)
        cerrar_conexion(conexion)
        if exito:
            print("✅ Insumo modificado correctamente.")
        else:
            print("❌ No se pudo modificar el insumo.")

def baja_insumo():
    print("=== Baja de Insumo ===")
    id = input("ID del Insumo a eliminar: ")

    conexion = crear_conexion()
    if conexion:
        exito = eliminar_insumo(conexion, id)
        cerrar_conexion(conexion)
        if exito:
            print("✅ Insumo eliminado correctamente.")
        else:
            print("❌ No se pudo eliminar el insumo.")

def listar_insumos():
    print("=== Lista de Insumos ===")
    conexion = crear_conexion()
    if conexion:
        clientes = mostrar_insumos(conexion)
        cerrar_conexion(conexion)

        if insumos:
            for i in insumos:
                print(f"ID: {i[0]} | Nombre: {i[1]} | Dirección: {c[2]} | Tel: {c[3]} | Correo: {c[4]}")
        else:
            print("No se encontraron insumos.")
