#Maneja altas, bajas, modificaciones y consultas de insumos.(insert, update, delete y select)

import mysql.connector
from backend.db.conexion import crear_conexion, cerrar_conexion
from backend.db.queries.insumos-queries import (
    INSERTAR_INSUMO,
    EDITAR_INSUMO,
    ELIMINAR_INSUMO,
    LISTAR_INSUMO
)
