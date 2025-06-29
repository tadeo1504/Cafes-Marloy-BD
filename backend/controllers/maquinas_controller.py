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
    modelo = input("Modelo: ")
    id_cliente = input("id cliente: ")
    ubicacion_cliente = input("ubicacion cliente: ")
    costo_alquiler_mensual = input("costo mensual: ")

    conexion = crear_conexion(tipo="admin")
    if conexion:
        exito = insertar_maquina(conexion, modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual)
        cerrar_conexion(conexion)
        if exito:
            print("Maquina insertado correctamente.")
        else:
            print("No se pudo insertar la maquina.")
            
def modificar_maquina():
    print("=== Modificación de maquina ===")
    id = input("ID de la maquina a modificar: ")
    id_cliente = input("cambio id cliente: ")
    modelo = input("Cambio del modelo: ")
    ubicacion_cliente = input("Nueva ubicación cliente: ")
    costo_alquiler_mensual = input("Nuevo costo mensual: ")

    if id == "" or id_cliente == "" or modelo == "" or ubicacion_cliente == "" or costo_alquiler_mensual == "":
        print("❌ Todos los campos son obligatorios.")
        return

    conexion = crear_conexion(tipo="admin")
    if conexion:
        exito = editar_maquina(conexion, id, id_cliente, modelo, ubicacion_cliente, costo_alquiler_mensual)
        cerrar_conexion(conexion)
        if exito:
            print("✅ Maquina modificado correctamente.")
        else:
            print("❌ No se pudo modificar la maquina.")

def baja_maquina():
    print("=== Baja de maquina ===")
    id = int(input("ID de la maquina a eliminar: ") )

    conexion = crear_conexion(tipo="admin")
    if conexion:
        exito = eliminar_maquina(conexion, id)
        cerrar_conexion(conexion)
        if exito:
            print("Maquina eliminada correctamente.")
        else:
            print("No se pudo eliminar la maquina.")
            

def listar_maquinas():
    print("=== Lista de Maquinas ===")
    conexion = crear_conexion(tipo="admin")
    if conexion:
        resultado = mostrar_maquinas(conexion)
        cerrar_conexion(conexion)

        if resultado["ok"]:
            maquinas = resultado["data"]
            if maquinas:
                for m in maquinas:
                    print(f"ID: {m['id']} | Modelo: {m['modelo']} | id_cliente: {m['id_cliente']} | ubicacion_cliente: {m['ubicacion_cliente']} | costo_alquiler_mensual: {m['costo_alquiler_mensual']}")
            else:
                print("No se encontraron maquinas.")
        else:
            print("❌ Error:", resultado["error"])



