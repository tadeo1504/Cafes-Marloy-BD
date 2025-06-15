# Maneja altas, bajas, modificaciones y consultas de maquinas.(insert, update, delete y select)

import mysql.connector
from backend.db.conexion import crear_conexion, cerrar_conexion
from backend.db.queries.maquinas_queries import (
    insertar_maquina,
    editar_maquina,
    eliminar_maquina,
    mostrar_maquinas
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
    id = input("ID de la maquina a modificar: ")
    nombre = input("Nuevo Nombre: ")
    direccion = input("Nueva Dirección: ")
    telefono = input("Nuevo Teléfono: ")
    correo = input("Nuevo Correo: ")

    conexion = crear_conexion()
    if conexion:
        exito = editar_maquina(conexion, id, nombre, direccion, telefono, correo)
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
            

def listar_maquinas():
    print("=== Lista de Maquinas ===")
    conexion = crear_conexion()
    if conexion:
        maquinas = mostrar_maquinas(conexion)
        cerrar_conexion(conexion)

        if maquinas:
            for m in maquinas:
                print(f"ID: {m[0]} | Modelo: {m[1]} | id_cliente: {m[2]} | ubicacion_cliente: {m[3]} | costo_alquiler_mensual: {m[4]}")
        else:
            print("No se encontraron maquinas.")


