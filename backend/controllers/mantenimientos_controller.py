#administrar alta baja modificacion y consulta de mantenimientos
#es decir insert, update, delete y select

import mysql.connector
from backend.db.conexion import crear_conexion, cerrar_conexion
from backend.db.queries.mantenimientos-queries import (
    INSERTAR_MANTENIMIENTO,
    EDITAR_MANTENIMIENTO,
    ELIMINAR_MANTENIMIENTO,
    LISTAR_MANTENIMIENTOS
 )

def alta_mantenimiento():
    pass

def modificacion_mantenimiento():
    pass

def baja_mantenimiento():
    pass

def listar_mantenimientos():
    pass
