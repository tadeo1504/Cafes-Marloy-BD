import mysql.connector
from mysql.connector import errorcode

# Configuración de conexión (ajustá según tu entorno)
config = {
    'user': '', # Cambiar esto por usuario de MySQL
    'password': '', # Cambiar esto por contraseña de MySQL
    'host': 'localhost',  # o 127.0.0.1
    'raise_on_warnings': True,
  #  'allow_multi_statements': True  # esto es xa ejecutar muchas queries juntas
}

# Leé el archivo SQL
with open("backend/db/CREATE_TABLES.sql", "r") as f:
    script_sql = f.read()

# Separar las sentencias (cuidado con los `DELIMITER` si tenés triggers)
sentencias = script_sql.split(';')

try:
    conn = mysql.connector.connect(**config)
    print("Conectado correctamente a MySQL...")
    cursor = conn.cursor()

    for sentencia in sentencias:
        stmt = sentencia.strip()
        if stmt:
            try:
                cursor.execute(stmt)
            except Exception as e:
                print(f"Error ejecutando sentencia:\n{stmt}\n→ {e}")

    conn.commit()
    print("Base de datos y tablas creadas con éxito.")

except mysql.connector.Error as err:
    print(f"Error de conexión: {err}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
