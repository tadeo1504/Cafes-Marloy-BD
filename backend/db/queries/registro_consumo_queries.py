#registro consumo

import mysql.connector

def insertar_registro_consumo(conexion, id_maquina, id_insumo, cantidad_usada):
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor()
        consulta = '''insert into registro_consumo (id_maquina, id_insumo, cantidad_usada) values (%s, %s, %s) '''
        cursor.execute(consulta,(id_maquina, id_insumo, cantidad_usada))
        conexion.commit()
        return {"ok": True}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}


def editar_registro_consumo(conexion, id, id_maquina, id_insumo, fecha, cantidad_usada):
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor()
        consulta = """
            UPDATE registro_consumo
            SET id_maquina = %s, id_insumo = %s, fecha = %s, cantidad_usada = %s
            WHERE id = %s
        """
        cursor.execute(consulta, (id_maquina, id_insumo, fecha, cantidad_usada, id))
        conexion.commit()
        return {"ok": True, "updated": cursor.rowcount}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}


def eliminar_registro_consumo(conexion, id):
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor()
        consulta = "DELETE FROM registro_consumo WHERE id = %s"
        cursor.execute(consulta, (id,))
        conexion.commit()
        return {"ok": True, "deleted": cursor.rowcount}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}


def mostrar_registros_consumo(conexion):
    if not conexion:
        return {"ok": False, "error": "No se pudo conectar a la BD"}
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM registro_consumo")
        resultados = cursor.fetchall()
        return {"ok": True, "data": resultados}
    except mysql.connector.Error as e:
        return {"ok": False, "error": str(e)}