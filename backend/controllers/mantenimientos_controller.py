#Maneja altas, bajas, modificaciones y consultas de mantenimientos.(insert, update, delete y select)

import mysql.connector
from backend.db.conexion import crear_conexion, cerrar_conexion
from backend.db.queries.mantenimientos_queries import (
    insertar_mantenimiento,
    editar_mantenimiento,
    eliminar_mantenimiento,
    mostrar_mantenimientos
)

def alta_mantenimiento():
    print("=== Alta de Mantenimiento ===")
    id_maquina = input("ID Maquina: ")
    ci_tecnico = input("CI Tecnico: ")
    fecha = input("Fecha: ")
    tipo = input("Tipo: ")
    observaciones = input("Observaciones: ")

    conexion = crear_conexion()
    if conexion:
        exito = insertar_mantenimiento(conexion, id_maquina, ci_tecnico, fecha, tipo, observaciones)
        # cerrar_conexion(conexion)
        if exito:
            print("Mantenimiento insertado correctamente.")
        else:
            print("❌ No se pudo insertar el mantenimiento.")
            
def modificar_mantenimiento():
    print("=== Modificación de mantenimiento ===")
    id = input("ID del mantenimiento a modificar: ")
    id_maquina = input("ID Maquina: ")
    ci_tecnico = input("CI Tecnico: ")
    fecha = input("Fecha: ")
    tipo = input("Tipo: ")
    observaciones = input("Observaciones: ")

    conexion = crear_conexion()
    if conexion:
        exito = editar_mantenimiento(conexion, id, id_maquina, ci_tecnico, fecha, tipo, observaciones)
        cerrar_conexion(conexion)
        if exito:
            print("Mantenimiento modificado correctamente.")
        else:
            print("❌ No se pudo modificar el mantenimiento.")

def baja_mantenimiento():
    print("=== Baja de mantenimiento ===")
    id = input("ID del mantenimiento a eliminar: ")

    conexion = crear_conexion()
    if conexion:
        exito = eliminar_mantenimiento(conexion, id)
        cerrar_conexion(conexion)
        if exito:
            print("Mantenimiento eliminado correctamente.")
        else:
            print("❌ No se pudo eliminar el mantenimiento.")
            

def listar_mantenimientos():
    print("=== Lista de mantenimientos ===")
    conexion = crear_conexion()
    if conexion:
        mantenimientos = mostrar_mantenimientos(conexion)
        cerrar_conexion(conexion)

        if mantenimientos:
            for m in mantenimientos:
                print(f"ID: {m['id']} | ID Maquina: {m['id_maquina']} | CI Tecnico: {m['ci_tecnico']} | Fecha: {m['fecha']} | Tipo: {m['tipo']} | Observaciones: {m['observaciones']}")
        else:
            print("❌ No se encontraron mantenimiento.")
