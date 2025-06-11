# Maneja altas, bajas, modificaciones y consultas de maquinas.(insert, update, delete y select)

import mysql.connector
from backend.db.conexion import crear_conexion, cerrar_conexion
from backend.db.queries.maquinas_queries import (
    INSERTAR_MAQUINA,
    EDITAR_MAQUINA,
    ELIMINAR_MAQUINA,
    LISTAR_MAQUINAS
)


def alta_maquina():
    print("=== Alta de maquina ===")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")

    conexion = crear_conexion()
    if conexion:
        exito = insertar_maquina(conexion, nombre, direccion, telefono, correo)
        cerrar_conexion(conexion)
        if exito:
            print("Maquina insertado correctamente.")
        else:
            print("No se pudo insertar la maquina.")
            
def modificar_maquina():
    print("=== Modificación de maquina ===")
    id_maquina = input("ID de la maquina a modificar: ")
    nombre = input("Nuevo Nombre: ")
    direccion = input("Nueva Dirección: ")
    telefono = input("Nuevo Teléfono: ")
    correo = input("Nuevo Correo: ")

    conexion = crear_conexion()
    if conexion:
        exito = editar_maquina(conexion, id_cliente, nombre, direccion, telefono, correo)
        cerrar_conexion(conexion)
        if exito:
            print("Maquina modificado correctamente.")
        else:
            print("No se pudo modificar la maquina.")
            
def baja_maquina():
    print("=== Baja de maquina ===")
    id_maquina = input("ID de la maquina a eliminar: ")

    conexion = crear_conexion()
    if conexion:
        exito = eliminar_maquina(conexion, id_maquina)
        cerrar_conexion(conexion)
        if exito:
            print("Maquina eliminada correctamente.")
        else:
            print("No se pudo eliminar la maquina.")
            

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
