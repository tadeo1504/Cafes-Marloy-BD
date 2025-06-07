#Maneja altas, bajas, modificaciones y consultas de insumos.(insert, update, delete y select)

import mysql.connector
from backend.db.conexion import crear_conexion, cerrar_conexion
from backend.db.queries.insumos-queries import (
    INSERTAR_INSUMO,
    EDITAR_INSUMO,
    ELIMINAR_INSUMO,
    LISTAR_INSUMO
)

def alta_insumo():
    print("=== Alta de Insumo ===")
    descripcion = input("Descripción: ")
    tipo = input("Tipo: ")
    precio_unitario = input("Precio unitario: ")
    id_proveedor = input("Id del Proveedor: ")

    conexion = crear_conexion()
    if conexion:
        exito = insertar_insumo(conexion, nombre, direccion, telefono, correo)
        cerrar_conexion(conexion)
        if exito:
            print("Insumo insertado correctamente.")
        else:
            print("No se pudo insertar el insumo.")
