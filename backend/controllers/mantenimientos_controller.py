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
    # fecha = input("Fecha: ")
    tipo = input("Tipo: ")
    observaciones = input("Observaciones: ")

    if id_maquina == "" or ci_tecnico == "" or tipo == "" or observaciones == "":
        print("❌ Los campos ID Maquina, CI Tecnico, Tipo y Observaciones son obligatorios.")
        return

    conexion = crear_conexion()
    if conexion:
        exito = insertar_mantenimiento(conexion, id_maquina, ci_tecnico, tipo, observaciones)
        cerrar_conexion(conexion)
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

    if id == "" or id_maquina == "" or ci_tecnico == "" or fecha == "" or tipo == "" or observaciones == "":
        print("❌ Todos los campos son obligatorios.")
        return

    conexion = crear_conexion(tipo="admin")
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

    conexion = crear_conexion(tipo="admin")
    if conexion:
        exito = eliminar_mantenimiento(conexion, id)
        cerrar_conexion(conexion)
        if exito:
            print("Mantenimiento eliminado correctamente.")
        else:
            print("❌ No se pudo eliminar el mantenimiento.")
            

def listar_mantenimientos():
    print("=== Lista de mantenimientos ===")
    conexion = crear_conexion(tipo="admin")
    if conexion:
        mantenimientos = mostrar_mantenimientos(conexion)
        cerrar_conexion(conexion)

        if mantenimientos.get("ok"):
            mantenimientos = mantenimientos.get("data")
        else:
            print(f"❌ Error al obtener mantenimientos: {mantenimientos.get('error')}")
            return

        if mantenimientos:
            for m in mantenimientos:
                print(f"ID: {m['id']} | ID Maquina: {m['id_maquina']} | CI Tecnico: {m['ci_tecnico']} | Fecha: {m['fecha']} | Tipo: {m['tipo']} | Observaciones: {m['observaciones']}")
        else:
            print("❌ No se encontraron mantenimiento.")
