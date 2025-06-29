import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()

def crear_conexion(tipo='comun'):
    try:
        if tipo == 'admin':
            user = os.getenv("DB_ADMIN_USER")
            password = os.getenv("DB_ADMIN_PASSWORD")
        else:
            user = os.getenv("DB_USER_COMUN")
            password = os.getenv("DB_PASSWORD_COMUN")

        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=user,
            password=password,
            database=os.getenv("DB_NAME")
        )

        if conexion.is_connected():
            print(f"✅ Conexión ({tipo}) a la base de datos MySQL exitosa")
            return conexion
    except Error as e:
        print(f"❌ Error al conectar ({tipo}) a la base de datos: {e}")
    return None

def cerrar_conexion(conexion):
    if conexion and conexion.is_connected():
        conexion.close()
        print("🔌 Conexión cerrada")
