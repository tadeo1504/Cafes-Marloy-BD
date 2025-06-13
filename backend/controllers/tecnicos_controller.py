#maneja altas, bajas, modificaciones y consultas de clientes
#es decir insert, update, delete y select
# Solo para administradores.

import mysql.connector
from backend.db.conexion import crear_conexion, cerrar_conexion
from backend.db.queries.tecnicos_queries import (
    insertar_tecnico,
    editar_tecnico,
    eliminar_tecnico,
    listar_tecnicos
)


def alta_tecnico():
    print("=== Alta de tecnico ===")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")

    conexion = crear_conexion()
    if conexion:
        exito = insertar_tecnico(conexion, nombre, direccion, telefono, correo)
        cerrar_conexion(conexion)
        if exito:
            print("Tecnico insertado correctamente.")
        else:
            print("No se pudo insertar el tecnico.")
            
def modificar_tecnico():
    print("=== Modificación de Tecnico ===")
    id_tecnico = input("ID del tecnico a modificar: ")
    nombre = input("Nuevo Nombre: ")
    direccion = input("Nueva Dirección: ")
    telefono = input("Nuevo Teléfono: ")
    correo = input("Nuevo Correo: ")

    conexion = crear_conexion()
    if conexion:
        exito = editar_tecnico(conexion, id_tecnico, nombre, direccion, telefono, correo)
        cerrar_conexion(conexion)
        if exito:
            print("Tecnico modificado correctamente.")
        else:
            print("No se pudo modificar el tecnico.")
            
def baja_tecnico():
    print("=== Baja de tecnico ===")
    id_tecnico = input("ID del tecnico a eliminar: ")

    conexion = crear_conexion()
    if conexion:
        exito = eliminar_tecnico(conexion, id_tecnico)
        cerrar_conexion(conexion)
        if exito:
            print("Tecnico eliminado correctamente.")
        else:
            print("No se pudo eliminar el tecnico.")
            

def mostrar_tecnicos():
    print("=== Lista de tecnicos ===")
    conexion = crear_conexion()
    if conexion:
        tecnicos = listar_tecnicos(conexion)
        cerrar_conexion(conexion)

        if tecnicos:
            for t in tecnicos:
                print(f"ID: {c[0]} | Nombre: {c[1]} | Dirección: {c[2]} | Tel: {c[3]} | Correo: {c[4]}")
        else:
            print("No se encontraron tecnicos.")
