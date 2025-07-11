# Maneja altas, bajas, modificaciones y consultas de tecnicos. (insert, update, delete y select)
# Solo para administradores.

import mysql.connector
from backend.db.conexion import crear_conexion, cerrar_conexion
from backend.db.queries.tecnicos_queries import (
    insertar_tecnico,
    editar_tecnico,
    eliminar_tecnico,
    mostrar_tecnicos
)


def alta_tecnico():
    print("=== Alta de tecnico ===")
    ci = input("Ci: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    
    conexion = crear_conexion(tipo="admin")
    if conexion:
        exito = insertar_tecnico(conexion, ci, nombre, apellido, telefono)
        cerrar_conexion(conexion)
        if exito:
            print("Tecnico insertado correctamente.")
        else:
            print("No se pudo insertar el tecnico.")
            
def modificar_tecnico():
    print("=== Modificación de Tecnico ===")
    ci = input("CI del tecnico a modificar: ")
    nombre = input("Nuevo Nombre: ")
    apellido = input("Nuevo Apellido: ")
    telefono = input("Nuevo Teléfono: ")

    conexion = crear_conexion(tipo="admin")
    if conexion:
        exito = editar_tecnico(conexion, ci, nombre, apellido, telefono)
        cerrar_conexion(conexion)
        if exito:
            print("Tecnico modificado correctamente.")
        else:
            print("No se pudo modificar el tecnico.")
            
def baja_tecnico():
    print("=== Baja de tecnico ===")
    ci = input("CI del tecnico a eliminar: ")

    conexion = crear_conexion(tipo="admin")
    if conexion:
        exito = eliminar_tecnico(conexion, ci)
        cerrar_conexion(conexion)
        if exito:
            print("Tecnico eliminado correctamente.")
        else:
            print("No se pudo eliminar el tecnico.")
            

def listar_tecnicos():
    print("=== Lista de tecnicos ===")
    conexion = crear_conexion(tipo="admin")
    if conexion:
        tecnicos = mostrar_tecnicos(conexion)
        cerrar_conexion(conexion)
        if tecnicos.get('ok'):
            tecnicos = tecnicos.get('data')
        else:
            tecnicos = []
        if tecnicos:
            for t in tecnicos:
                print(f"CI: {t['ci']} | Nombre: {t['nombre']} | Apellido: {t['apellido']} | Tel: {t['telefono']}")
        else:
            print("No se encontraron tecnicos.")
