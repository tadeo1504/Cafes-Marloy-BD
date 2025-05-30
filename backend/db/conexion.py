import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import Error

# Cargar las variables del archivo .env
load_dotenv()

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        if conexion.is_connected():
            print("✅ Conexión a la base de datos MySQL exitosa")
            return conexion
    except Error as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
    return None

def ejecutar_consulta(conexion, consulta):
    try:
        cursor = conexion.cursor()
        cursor.execute(consulta)
        conexion.commit()
        print("✅ Consulta ejecutada exitosamente")
        return True
    except Error as e:
        print(f"❌ Error al ejecutar la consulta: {e}")
        return False

def cerrar_conexion(conexion):
    if conexion and conexion.is_connected():
        conexion.close()
        print("🔌 Conexión cerrada")
