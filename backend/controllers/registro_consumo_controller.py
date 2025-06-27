from backend.db.conexion import crear_conexion, cerrar_conexion
from backend.db.queries.registro_consumo_queries import (
    insertar_registro_consumo,
    editar_registro_consumo,
    eliminar_registro_consumo,
    mostrar_registros_consumo
)

def alta_registro_consumo():
    print("=== Alta de Registro de Consumo ===")
    id_maquina = input("ID de la Máquina: ")
    id_insumo = input("ID del Insumo: ")
    fecha = input("Fecha (YYYY-MM-DD): ")
    cantidad_usada = input("Cantidad Usada: ")

    conexion = crear_conexion()
    if conexion:
        resultado = insertar_registro_consumo(conexion, id_maquina, id_insumo, fecha, cantidad_usada)
        cerrar_conexion(conexion)
        if resultado["ok"]:
            print("✅ Registro de consumo insertado correctamente.")
        else:
            print(f"❌ No se pudo insertar el registro de consumo: {resultado['error']}")

def modificar_registro_consumo():
    print("=== Modificación de Registro de Consumo ===")
    id = input("ID del Registro a modificar: ")
    id_maquina = input("Nuevo ID de la Máquina: ")
    id_insumo = input("Nuevo ID del Insumo: ")
    fecha = input("Nueva Fecha (YYYY-MM-DD): ")
    cantidad_usada = input("Nueva Cantidad Usada: ")

    conexion = crear_conexion()
    if conexion:
        resultado = editar_registro_consumo(conexion, id, id_maquina, id_insumo, fecha, cantidad_usada)
        cerrar_conexion(conexion)
        if resultado["ok"]:
            print("✅ Registro de consumo modificado correctamente.")
        else:
            print(f"❌ No se pudo modificar el registro de consumo: {resultado['error']}")

def baja_registro_consumo():
    print("=== Baja de Registro de Consumo ===")
    id = input("ID del Registro a eliminar: ")

    conexion = crear_conexion()
    if conexion:
        resultado = eliminar_registro_consumo(conexion, id)
        cerrar_conexion(conexion)
        if resultado["ok"]:
            print("✅ Registro de consumo eliminado correctamente.")
        else:
            print(f"❌ No se pudo eliminar el registro de consumo: {resultado['error']}")

def listar_registros_consumo():
    print("=== Lista de Registros de Consumo ===")
    conexion = crear_conexion()
    if conexion:
        registros = mostrar_registros_consumo(conexion)
        cerrar_conexion(conexion)
        if registros:
            for registro in registros:
                print(f"ID: {registro[0]}, ID Máquina: {registro[1]}, ID Insumo: {registro[2]}, Fecha: {registro[3]}, Cantidad Usada: {registro[4]}")
        else:
            print("No hay registros de consumo disponibles.")
            