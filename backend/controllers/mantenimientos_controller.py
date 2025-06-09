#maneja altas, bajas, modificaciones y consultas de clientes
#es decir insert, update, delete y select

import mysql.connector
from backend.db.conexion import crear_conexion, cerrar_conexion
from backend.db.queries.mantenimientos_queries import (
    INSERTAR_MANTENIMIENTO,
    EDITAR_MANTENIMIENTO,
    ELIMINAR_MANTENIMIENTO,
    LISTAR_MANTENIMIENTOS
)


def alta_mantenimiento():
    print("=== Alta de Mantenimiento ===")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")

    conexion = crear_conexion()
    if conexion:
        exito = insertar_mantenimiento(conexion, nombre, direccion, telefono, correo)
        cerrar_conexion(conexion)
        if exito:
            print("Mantenimiento insertado correctamente.")
        else:
            print("No se pudo insertar el mantenimiento.")
            
def modificar_mantenimiento():
    print("=== Modificación de mantenimiento ===")
    id_cliente = input("ID del mantenimiento a modificar: ")
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
            
def baja_mantenimiento():
    print("=== Baja de mantenimiento ===")
    id_mantenimiento = input("ID del mantenimiento a eliminar: ")

    conexion = crear_conexion()
    if conexion:
        exito = eliminar_mantenimiento(conexion, id_mantenimiento)
        cerrar_conexion(conexion)
        if exito:
            print("Mantenimiento eliminado correctamente.")
        else:
            print("No se pudo eliminar el mantenimiento.")
            

def listar_mantenimientos():
    print("=== Lista de mantenimientos ===")
    conexion = crear_conexion()
    if conexion:
        mantenimientos = obtener_todos_los_mantenimientos(conexion)
        cerrar_conexion(conexion)

        if mantenimientos:
            for m in mantenimiento:
                print(f"ID: {m[0]} | Nombre: {c[1]} | Dirección: {c[2]} | Tel: {c[3]} | Correo: {c[4]}")
        else:
            print("No se encontraron mantenimiento.")
