#administrar alta baja modificacion y consulta de mantenimientos
##es decir insert, update, delete y select

import mysql.connector
from backend.db.conexion import crear_conexion, cerrar_conexion
<<<<<<< Updated upstream
#primero tiene que existir el archivo mantenimientos_querys.py en la carpeta db
# from backend.db.mantenimientos_querys import (
#     INSERTAR_MANTENIMIENTO,
#     EDITAR_MANTENIMIENTO,
#     ELIMINAR_MANTENIMIENTO,
#     LISTAR_MANTENIMIENTOS
# )
=======
from backend.db.queries.mantenimientos_queries import (
    INSERTAR_MANTENIMIENTO,
    EDITAR_MANTENIMIENTO,
    ELIMINAR_MANTENIMIENTO,
    LISTAR_MANTENIMIENTOS
 )
>>>>>>> Stashed changes

def alta_mantenimiento():
    pass

def modificacion_mantenimiento():
    pass

def baja_mantenimiento():
    pass

def listar_mantenimientos():
    pass
