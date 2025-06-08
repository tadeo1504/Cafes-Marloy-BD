#maneja altas, bajas, modificaciones y consultas de clientes
#es decir insert, update, delete y select

import mysql.connector
from backend.db.conexion import crear_conexion, cerrar_conexion
<<<<<<< Updated upstream
from backend.db.clientes_querys import (
=======
from backend.db.Queries.clientes_queries import (
>>>>>>> Stashed changes
    INSERTAR_CLIENTE,
    EDITAR_CLIENTE,
    ELIMINAR_CLIENTE,
    LISTAR_CLIENTES
)


def alta_cliente():
    print("=== Alta de Cliente ===")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")

    conexion = crear_conexion()
    if conexion:
        exito = insertar_cliente(conexion, nombre, direccion, telefono, correo)
        cerrar_conexion(conexion)
        if exito:
            print("Cliente insertado correctamente.")
        else:
            print("No se pudo insertar el cliente.")
            
def modificar_cliente():
    print("=== Modificación de Cliente ===")
    id_cliente = input("ID del Cliente a modificar: ")
    nombre = input("Nuevo Nombre: ")
    direccion = input("Nueva Dirección: ")
    telefono = input("Nuevo Teléfono: ")
    correo = input("Nuevo Correo: ")

    conexion = crear_conexion()
    if conexion:
        exito = editar_cliente(conexion, id_cliente, nombre, direccion, telefono, correo)
        cerrar_conexion(conexion)
        if exito:
            print("Cliente modificado correctamente.")
        else:
            print("No se pudo modificar el cliente.")
            
def baja_cliente():
    print("=== Baja de Cliente ===")
    id_cliente = input("ID del Cliente a eliminar: ")

    conexion = crear_conexion()
    if conexion:
        exito = eliminar_cliente(conexion, id_cliente)
        cerrar_conexion(conexion)
        if exito:
            print("Cliente eliminado correctamente.")
        else:
            print("No se pudo eliminar el cliente.")
            

def listar_clientes():
    print("=== Lista de Clientes ===")
    conexion = crear_conexion()
    if conexion:
        clientes = obtener_todos_los_clientes(conexion)
        cerrar_conexion(conexion)

        if clientes:
            for c in clientes:
                print(f"ID: {c[0]} | Nombre: {c[1]} | Dirección: {c[2]} | Tel: {c[3]} | Correo: {c[4]}")
        else:
            print("No se encontraron clientes.")

