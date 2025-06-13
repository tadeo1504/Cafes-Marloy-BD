#Maneja altas, bajas, modificaciones y consultas de mantenimientos.(insert, update, delete y select)

import mysql.connector
from backend.db.conexion import crear_conexion, cerrar_conexion
from backend.db.queries.mantenimientos_queries import (
    insertar_mantenimientos,
    editar_mantenimiento,
    eliminar_mantenimientos,
    listar_mantenimientos
)


def alta_mantenimiento():
    print("=== Alta de Mantenimiento ===")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")

    conexion = crear_conexion()
    if conexion:
        exito = insertar_mantenimientos(conexion, nombre, direccion, telefono, correo)
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
        exito = editar_mantenimiento(conexion, id_cliente, nombre, direccion, telefono, correo)
        cerrar_conexion(conexion)
        if exito:
            print("Mantenimiento modificado correctamente.")
        else:
            print("No se pudo modificar el mantenimiento.")

def baja_mantenimiento():
    print("=== Baja de mantenimiento ===")
    id_mantenimiento = input("ID del mantenimiento a eliminar: ")

    conexion = crear_conexion()
    if conexion:
        exito = eliminar_mantenimientos(conexion, id_mantenimiento)
        cerrar_conexion(conexion)
        if exito:
            print("Mantenimiento eliminado correctamente.")
        else:
            print("No se pudo eliminar el mantenimiento.")
            

def mostrar_mantenimientos():
    print("=== Lista de mantenimientos ===")
    conexion = crear_conexion()
    if conexion:
        mantenimientos = listar_mantenimientos(conexion)
        cerrar_conexion(conexion)

        if mantenimientos:
            for m in mantenimientos:
                print(f"ID: {m[0]} | Nombre: {m[1]} | Dirección: {m[2]} | Tel: {m[3]} | Correo: {m[4]}")
        else:
            print("No se encontraron mantenimiento.")
