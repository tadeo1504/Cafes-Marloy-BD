#maneja altas, bajas, modificaciones y consultas de clientes. (insert, update, delete y select)

import mysql.connector
from backend.db.conexion import crear_conexion, cerrar_conexion
from backend.db.queries.clientes_queries import (
    insertar_cliente,
    editar_cliente,
    eliminar_cliente,
    mostrar_clientes
)


def alta_cliente():
    print("=== Alta de Cliente ===")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")

    if (nombre == ''):
        print("❌ El nombre es obligatorio.")
        return

    conexion = crear_conexion()
    if conexion:
        exito = insertar_cliente(conexion, nombre, direccion, telefono, correo)
        cerrar_conexion(conexion)
        if exito:
            print("✅ Cliente insertado correctamente.")
        else:
            print("❌ No se pudo insertar el cliente.")

def modificar_cliente():
    print("=== Modificación de Cliente ===")
    id = input("ID del Cliente a modificar: ")
    nombre = input("Nuevo Nombre: ")
    direccion = input("Nueva Dirección: ")
    telefono = input("Nuevo Teléfono: ")
    correo = input("Nuevo Correo: ")

    if id == "" or nombre == "" or direccion == "" or telefono == "" or correo == "":
        print("❌ Todos los campos son obligatorios.")
        return
    
    conexion = crear_conexion()
    if conexion:
        exito = editar_cliente(conexion, nombre, direccion, telefono, correo, id)
        cerrar_conexion(conexion)
        if exito:
            print("✅ Cliente modificado correctamente.")
            return True
        else:
            print("❌ No se pudo modificar el cliente.")

def baja_cliente():
    print("=== Baja de Cliente ===")
    id = input("ID del Cliente a eliminar: ")

    conexion = crear_conexion()
    if conexion:
        exito = eliminar_cliente(conexion, id)
        cerrar_conexion(conexion)
        if exito:
            print("✅ Cliente eliminado correctamente.")
            return True
        else:
            print("❌ No se pudo eliminar el cliente.")

def listar_clientes():
    print("=== Lista de Clientes ===")
    conexion = crear_conexion()
    if conexion:
        clientes = mostrar_clientes(conexion)
        cerrar_conexion(conexion)
        if clientes.get('ok'):
            clientes = clientes.get('data')
        else:
            clientes = []
    

        if clientes:
            for c in clientes:
                print(f"ID: {c['id']} | Nombre: {c['nombre']} | Dirección: {c['direccion']} | Tel: {c['telefono']} | Correo: {c['correo']}")
            return clientes
        else:
            print("❌ No se encontraron clientes.")
            return {"ok": False, "mensaje": "No se encontraron clientes."}

