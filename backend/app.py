# archivo: app.py
# python -m backend.app

#importar flask y otros módulos necesarios
from flask import Flask, request, jsonify
from flask_cors import CORS  # para permitir acceso desde el frontend

# importar conexión a la base de datos
from backend.db.conexion import crear_conexion, cerrar_conexion

from backend.controllers.auth_controller import login_usuario, registrar_usuario
from backend.db.queries.clientes_queries import insertar_cliente, editar_cliente, eliminar_cliente, mostrar_clientes
from backend.db.queries.insumos_queries import insertar_insumo, editar_insumo, eliminar_insumo, mostrar_insumos
from backend.db.queries.mantenimientos_queries import insertar_mantenimiento, editar_mantenimiento, eliminar_mantenimiento, mostrar_mantenimientos
from backend.db.queries.maquinas_queries import insertar_maquina, editar_maquina, eliminar_maquina, mostrar_maquinas
from backend.db.queries.proveedores_queries import insertar_proveedor, editar_proveedor, eliminar_proveedor, mostrar_proveedores
from backend.db.queries.registro_consumo_queries import insertar_registro_consumo, editar_registro_consumo, eliminar_registro_consumo, mostrar_registros_consumo
from backend.controllers.reportes_controller import reporte_total_mensual_por_cliente, reporte_insumos_mas_consumidos, reporte_tecnicos_mas_mantenimientos, reporte_clientes_con_mas_maquinas
from backend.db.queries.tecnicos_queries import insertar_tecnico, editar_tecnico, eliminar_tecnico, mostrar_tecnicos

# importar el decorador de autenticación
from backend.auth.decorators import solo_admin  # importar el decorador


app = Flask(__name__)
CORS(app)  # permite peticiones desde el navegador

# === mini indice de rutas ===
#auth
#clientes
#insumos
#mantenimientos
#maquinas
#proveedores
#registro_consumo
#reportes
#tecnicos


# === AUTENTICACIÓN  ===

@app.route('/api/usuarios/login', methods=['POST'])
def login():
    data = request.json
    correo = data.get('correo')
    contrasena = data.get('contrasena')

    if not correo or not contrasena:
        return jsonify({"ok": False, "mensaje": "Correo y contraseña son obligatorios"}), 400

    if len(correo) > 100 or len(contrasena) > 100:
        return jsonify({"ok": False, "mensaje": "Los campos exceden el largo permitido"}), 400

    resultado = login_usuario(correo, contrasena)

    if resultado.get("success"):
        return jsonify({
            "ok": True,
            "usuario": resultado["usuario"],
            "token": resultado["token"]
        })
    else:
        return jsonify({"ok": False, "error": resultado["error"]}), 401

@app.route('/api/usuarios/registro', methods=['POST'])
def registro():
    data = request.json
    correo = data.get('correo')
    contrasena = data.get('contrasena')
    es_administrador = data.get('admin', 0)

    if not correo or not contrasena:
        return jsonify({"ok": False, "mensaje": "Correo y contraseña son obligatorios"}), 400

    if len(correo) > 100 or len(contrasena) > 100:
        return jsonify({"ok": False, "mensaje": "Los campos exceden el largo permitido"}), 400

    resultado = registrar_usuario(correo, contrasena, es_administrador)

    if resultado.get("success"):
        return jsonify({"ok": True, "mensaje": "Usuario registrado correctamente"})
    return jsonify({"ok": False, "error": resultado.get("error", "Error al registrar")}), 400


# === CLIENTES ===

@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    clientes = mostrar_clientes(conexion)
    cerrar_conexion(conexion)

    return (clientes),200


@app.route('/api/clientes', methods=['POST'])
def post_cliente():
    data = request.json
    required_fields = ["nombre", "direccion", "telefono", "correo"]
    if not all(data.get(field) for field in required_fields):
        return jsonify({"ok": False, "mensaje": "Faltan campos requeridos"}), 400

    if any(len(str(data.get(f))) > 100 for f in ["nombre", "direccion", "telefono", "correo"]):
        return jsonify({"ok": False, "mensaje": "Algún campo excede el largo máximo permitido"}), 400

    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = insertar_cliente(
        conexion,
        data.get("nombre"),
        data.get("direccion"),
        data.get("telefono"),
        data.get("correo")
    )
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Cliente insertado correctamente"}), 201
    return jsonify({"ok": False, "mensaje": "No se pudo insertar el cliente"}), 400


@app.route('/api/clientes/<int:id>', methods=['PUT'])
def put_cliente(id):
    data = request.json
    required_fields = ["nombre", "direccion", "telefono", "correo"]
    if not all(data.get(field) for field in required_fields):
        return jsonify({"ok": False, "mensaje": "Faltan campos requeridos"}), 400

    if any(len(str(data.get(f))) > 100 for f in ["nombre", "direccion", "telefono", "correo"]):
        return jsonify({"ok": False, "mensaje": "Algún campo excede el largo máximo permitido"}), 400

    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = editar_cliente(
        conexion=conexion,
        nombre=data.get("nombre"),
        direccion=data.get("direccion"),
        telefono=data.get("telefono"),
        correo=data.get("correo"),
        id=id
    )
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Cliente modificado correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo modificar el cliente"}), 400


@app.route('/api/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id):

    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = eliminar_cliente(conexion, (id))
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Cliente eliminado correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo eliminar el cliente"}), 400


# === INSUMOS ===

@app.route('/api/insumos', methods=['GET'])
def get_insumos():
    conexion = crear_conexion()  
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    insumos = mostrar_insumos(conexion)
    cerrar_conexion(conexion)

    return jsonify(insumos)

@app.route('/api/insumos', methods=['POST'])
def post_insumo():
    data = request.json
    required_fields = ["tipo", "descripcion", "precio_unitario", 'id_proveedor']
    if not all(data.get(field) for field in required_fields):
        return jsonify({"ok": False, "mensaje": "Faltan campos requeridos"}), 400

    if any(len(str(data.get(f))) > 100 for f in ["tipo", "descripcion"]):
        return jsonify({"ok": False, "mensaje": "Algún campo de texto excede el largo permitido"}), 400

    try:
        precio_unitario = float(data.get("precio_unitario"))
        id_proveedor = int(data.get("id_proveedor"))
    except (ValueError, TypeError):
        return jsonify({"ok": False, "mensaje": "precio_unitario debe ser numérico y id_proveedor un entero"}), 400

    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = insertar_insumo(
        conexion=conexion,
        tipo=data.get("tipo"),
        descripcion=data.get("descripcion"),
        precio_unitario=precio_unitario,
        id_proveedor=id_proveedor
    )

    cerrar_conexion(conexion)

    if exito:
        return jsonify({"ok": True, "mensaje": "Insumo insertado correctamente"}), 201
    return jsonify({"ok": False, "mensaje": "No se pudo insertar el insumo"}), 400

@app.route('/api/insumos/<int:id>', methods=['PUT'])
def put_insumo(id):
    data = request.json
    required_fields = ["tipo", "descripcion", "precio_unitario", "id_proveedor"]
    if not all(data.get(field) for field in required_fields):
        return jsonify({"ok": False, "mensaje": "Faltan campos requeridos"}), 400

    if any(len(str(data.get(f))) > 100 for f in ["tipo", "descripcion"]):
        return jsonify({"ok": False, "mensaje": "Algún campo de texto excede el largo permitido"}), 400

    try:
        precio_unitario = float(data.get("precio_unitario"))
        id_proveedor = int(data.get("id_proveedor"))
    except (ValueError, TypeError):
        return jsonify({"ok": False, "mensaje": "precio_unitario debe ser numérico y id_proveedor un entero"}), 400
    if not id or id <= 0:   
        return jsonify({"ok": False, "mensaje": "ID inválido"}), 400

    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = editar_insumo(
        conexion=conexion,
        tipo=data.get("tipo"),
        descripcion=data.get("descripcion"),
        precio_unitario=data.get("precio_unitario"),
        id_proveedor=data.get("id_proveedor"),
        id=id
    )
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Insumo modificado correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo modificar el insumo"}), 400

@app.route('/api/insumos/<int:id>', methods=['DELETE'])
def delete_insumo(id):
    conexion = crear_conexion()  
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = eliminar_insumo(conexion, (id))
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Insumo eliminado correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo eliminar el insumo"}), 400



# === MANTENIMIENTOS ===



@app.route('/api/mantenimientos', methods=['GET'])
def get_mantenimientos():
    conexion = crear_conexion() 
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    mantenimientos = mostrar_mantenimientos(conexion)
    cerrar_conexion(conexion)

    return jsonify(mantenimientos)

@app.route('/api/mantenimientos', methods=['POST'])
def post_mantenimiento():
    data = request.json
    conexion = crear_conexion(tipo="admin")  # solo los administradores pueden acceder a esta ruta
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500
    
    required_fields = ["id_maquina", "tipo", "ci_tecnico", "observaciones"]
    if not all(data.get(field) for field in required_fields):
        return jsonify({"ok": False, "mensaje": "Faltan campos requeridos"}), 400
    if any(len(str(data.get(f))) > 100 for f in ["tipo", "observaciones"]):
        return jsonify({"ok": False, "mensaje": "Algún campo de texto excede el largo permitido"}), 400
    try:
        id_maquina = int(data.get("id_maquina"))
        ci_tecnico = int(data.get("ci_tecnico"))

    except (ValueError, TypeError):
        return jsonify({"ok": False, "mensaje": "id_maquina y ci_tecnico deben ser numéricos"}), 400

    if not id_maquina or id_maquina <= 0 or not ci_tecnico or ci_tecnico <= 0:
        return jsonify({"ok": False, "mensaje": "ID de máquina o CI de técnico inválidos"}), 400
    
    exito = insertar_mantenimiento(
        conexion=conexion,
        id_maquina=data.get("id_maquina"),
        tipo=data.get("tipo"),
        ci_tecnico=data.get("ci_tecnico"),
        observaciones=data.get("observaciones")
    )
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Mantenimiento insertado correctamente"}), 201
    return jsonify({"ok": False, "mensaje": "No se pudo insertar el mantenimiento"}), 400

@app.route('/api/mantenimientos/<int:id>', methods=['PUT'])
def put_mantenimiento(id):
    data = request.json
    conexion = crear_conexion(tipo="admin")
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = editar_mantenimiento(
        conexion=conexion,
        fecha=data.get("fecha"),
        descripcion=data.get("descripcion"),
        costo=data.get("costo"),
        proveedor_id=data.get("proveedor_id"),
        id=id
    )
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Mantenimiento modificado correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo modificar el mantenimiento"}), 400

@app.route('/api/mantenimientos/<int:id>', methods=['DELETE'])
def delete_mantenimiento(id):
    conexion = crear_conexion(tipo="admin")  # solo los administradores pueden acceder a esta ruta
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = eliminar_mantenimiento(conexion, (id))
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Mantenimiento eliminado correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo eliminar el mantenimiento"}), 400



# === MAQUINAS ===


@app.route('/api/maquinas', methods=['GET'])
#   # solo los administradores pueden acceder a esta ruta
def get_maquinas():
    conexion = crear_conexion(tipo="admin")  # solo los administradores pueden acceder a esta ruta
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    maquinas = mostrar_maquinas(conexion)
    cerrar_conexion(conexion)

    return jsonify(maquinas)

@app.route('/api/maquinas', methods=['POST'])
#   # solo los administradores pueden acceder a esta ruta
def post_maquina():
    data = request.json
    conexion = crear_conexion(tipo="admin")  # solo los administradores pueden acceder a esta ruta
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = insertar_maquina(
        conexion=conexion,
        modelo=data.get("modelo"),
        costo_alquiler_mensual=data.get("costo_alquiler_mensual"),
        ubicacion_cliente=data.get("ubicacion_cliente"),
        id_cliente=data.get("id_cliente")
    )
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Máquina insertada correctamente"}), 201
    return jsonify({"ok": False, "mensaje": "No se pudo insertar la máquina"}), 400

@app.route('/api/maquinas/<int:id>', methods=['PUT'])
#   # solo los administradores pueden acceder a esta ruta
def put_maquina(id):
    data = request.json
    print(data)
    conexion = crear_conexion(tipo="admin")  # solo los administradores pueden acceder a esta ruta
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = editar_maquina(
        conexion=conexion,
        id_cliente=data.get("id_cliente"),
        modelo=data.get("modelo"),
        costo_alquiler_mensual=data.get("costo_alquiler_mensual"),
        ubicacion_cliente=data.get("ubicacion_cliente"),
        id=id
    )
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Máquina modificada correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo modificar la máquina"}), 400

@app.route('/api/maquinas/<int:id>', methods=['DELETE'])
#   # solo los administradores pueden acceder a esta ruta
def delete_maquina(id):
    print(type(id))
    conexion = crear_conexion(tipo="admin")  # solo los administradores pueden acceder a esta ruta
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = eliminar_maquina(conexion, (id))
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Máquina eliminada correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo eliminar la máquina"}), 400



# === PROVEEDORES ===


@app.route('/api/proveedores', methods=['GET'])
#   # solo los administradores pueden acceder a esta ruta
def get_proveedores():
    conexion = crear_conexion(tipo="admin")
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    proveedores = mostrar_proveedores(conexion)
    cerrar_conexion(conexion)

    return jsonify(proveedores)

@app.route('/api/proveedores', methods=['POST'])
  # solo los administradores pueden acceder a esta ruta
def post_proveedor():
    data = request.json
    conexion = crear_conexion(tipo="admin")
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = insertar_proveedor(
        conexion=conexion,
        nombre=data.get("nombre"),
        contacto=data.get("")
    )
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Proveedor insertado correctamente"}), 201
    return jsonify({"ok": False, "mensaje": "No se pudo insertar el proveedor"}), 400

@app.route('/api/proveedores/<int:id>', methods=['PUT'])
  # solo los administradores pueden acceder a esta ruta
def put_proveedor(id):
    data = request.json
    conexion = crear_conexion(tipo="admin")
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = editar_proveedor(
        conexion=conexion,
        nombre=data.get("nombre"),
        contacto=data.get("contacto"),
        id=id
    )
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Proveedor modificado correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo modificar el proveedor"}), 400

@app.route('/api/proveedores/<int:id>', methods=['DELETE'])
  # solo los administradores pueden acceder a esta ruta
def delete_proveedor(id):
    conexion = crear_conexion(tipo="admin")
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = eliminar_proveedor(conexion, (id))
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Proveedor eliminado correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo eliminar el proveedor"}), 400



# === TÉCNICOS ===



@app.route('/api/tecnicos', methods=['GET'])
  # solo los administradores pueden acceder a esta ruta
def get_tecnicos():
    conexion = crear_conexion(tipo='admin')
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    tecnicos = mostrar_tecnicos(conexion)
    cerrar_conexion(conexion)

    return jsonify(tecnicos)

@app.route('/api/tecnicos', methods=['POST'])
def post_tecnico():
    data = request.json
    required_fields = ["ci", "nombre", "apellido", "telefono"]
    if not all(data.get(field) for field in required_fields):
        return jsonify({"ok": False, "mensaje": "Faltan campos requeridos"}), 400

    # Validar longitud
    if any(len(str(data.get(f))) > 100 for f in ["nombre", "apellido"]):
        return jsonify({"ok": False, "mensaje": "Nombre o apellido excede el largo permitido"}), 400

    if len(str(data.get("ci"))) > 20 or len(str(data.get("telefono"))) > 20:
        return jsonify({"ok": False, "mensaje": "CI o teléfono excede el largo permitido"}), 400

    try:
        ci = str(data.get("ci"))
    except Exception:
        return jsonify({"ok": False, "mensaje": "CI inválido"}), 400

    conexion = crear_conexion(tipo='admin')
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = insertar_tecnico(
        conexion=conexion,
        ci=ci,
        nombre=data.get("nombre"),
        apellido=data.get("apellido"),
        telefono=data.get("telefono")
    )
    cerrar_conexion(conexion)

    if exito:
        return jsonify({"ok": True, "mensaje": "Técnico insertado correctamente"}), 201
    return jsonify({"ok": False, "mensaje": "No se pudo insertar el técnico"}), 400


@app.route('/api/tecnicos/<int:ci>', methods=['PUT'])
  # solo los administradores pueden acceder a esta ruta
def put_tecnico(ci):
    data = request.json
    conexion = crear_conexion(tipo="admin")
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = editar_tecnico(
        conexion=conexion,
        nombre=data.get("nombre"),
        apellido=data.get("apellido"),
        telefono=data.get("telefono"),
        ci=ci
    )
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Técnico modificado correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo modificar el técnico"}), 400

@app.route('/api/tecnicos/<int:ci>', methods=['DELETE'])
  # solo los administradores pueden acceder a esta ruta
def delete_tecnico(ci):
    conexion = crear_conexion(tipo="admin")
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = eliminar_tecnico(conexion, (ci))
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Técnico eliminado correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo eliminar el técnico"}), 400



# === REGISTRO DE CONSUMO ===


@app.route('/api/registros_consumo', methods=['GET'])
def get_registros_consumo():
    conexion = crear_conexion(tipo="admin")  # solo los administradores pueden acceder a esta ruta
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    registros = mostrar_registros_consumo(conexion)
    cerrar_conexion(conexion)

    return jsonify(registros)

@app.route('/api/registros_consumo', methods=['POST'])
def post_registro_consumo():
    data = request.json

    required_fields = ["id_maquina", "id_insumo", "cantidad_usada"]
    if not all(field in data for field in required_fields):
        return jsonify({"ok": False, "mensaje": "Faltan campos requeridos"}), 400
    if any(len(str(data.get(f))) > 100 for f in ["fecha", "cantidad", "insumo_id", "cliente_id"]):
        return jsonify({"ok": False, "mensaje": "Algún campo excede el largo máximo permitido"}), 400
    try:
        data["cantidad_usada"] = int(data.get("cantidad_usada"))  # convertir a entero
        data["id_insumo"] = int(data.get("id_insumo"))  # convertir a entero
        data["id_maquina"] = int(data.get("id_maquina"))  # convertir a entero
    except (ValueError, TypeError):
        return jsonify({"ok": False, "mensaje": "cantidad_usada, id_insumo y id_maquina deben ser numéricos"}), 400

    conexion = crear_conexion(tipo="admin")
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = insertar_registro_consumo(
        conexion,
        data["id_maquina"],
        data["id_insumo"],
        data["cantidad_usada"]
    )
    cerrar_conexion(conexion)

    if exito:
        return jsonify({"ok": True, "mensaje": "Registro insertado correctamente"}), 201
    return jsonify({"ok": False, "mensaje": "No se pudo insertar el registro"}), 400

@app.route('/api/registros_consumo/<int:id>', methods=['PUT'])
def put_registro_consumo(id):
    data = request.json

    required_fields = ["id_maquina", "id_insumo", "cantidad_usada", 'fecha']
    if not all(field in data for field in required_fields):
        return jsonify({"ok": False, "mensaje": "Faltan campos requeridos"}), 400
    if any(len(str(data.get(f))) > 100 for f in ["fecha", "cantidad", "insumo_id", "cliente_id"]):
        return jsonify({"ok": False, "mensaje": "Algún campo excede el largo máximo permitido"}), 400
    try:
        data["cantidad"] = int(data.get("cantidad"))  # convertir a entero
        data["insumo_id"] = int(data.get("insumo_id"))  # convertir a entero
        data["id_maquina"] = int(data.get("id_maquina"))  # convertir a entero
    except (ValueError, TypeError):
        return jsonify({"ok": False, "mensaje": "cantidad, insumo_id y id_maquina deben ser numéricos"}), 400

    conexion = crear_conexion(tipo="admin")
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = editar_registro_consumo(
        conexion,
        data["fecha"],
        data["id_maquina"],
        data["id_insumo"],
        data["cantidad_usada"],
        id
    )
    cerrar_conexion(conexion)

    if exito:
        return jsonify({"ok": True, "mensaje": "Registro modificado correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo modificar el registro"}), 400

@app.route('/api/registros_consumo/<int:id>', methods=['DELETE'])
def delete_registro_consumo(id):
    conexion = crear_conexion(tipo="admin")
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = eliminar_registro_consumo(conexion, (id))
    cerrar_conexion(conexion)

    if exito:
        return jsonify({"ok": True, "mensaje": "Registro eliminado correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo eliminar el registro"}), 400


# === REPORTES ===

@app.route('/api/reportes/total-mensual-cliente', methods=['GET'])
def get_reporte_total_mensual_por_cliente():
    try:
        mes = int(request.args.get("mes"))
        anio = int(request.args.get("anio"))
        print(f"Mes: {mes}, Año: {anio}")
    except (TypeError, ValueError):
        return jsonify({"ok": False, "mensaje": "Parámetros inválidos"}), 400

    resultado = reporte_total_mensual_por_cliente(mes, anio)
    return jsonify(resultado)

@app.route('/api/reportes/insumos-mas-consumidos', methods=['GET'])
def get_insumos_mas_consumidos():
    resultado = reporte_insumos_mas_consumidos()
    return jsonify(resultado)

@app.route('/api/reportes/tecnicos-mas-mantenimientos', methods=['GET'])
def get_tecnicos_mas_mantenimientos():
    resultado = reporte_tecnicos_mas_mantenimientos()
    return jsonify(resultado)

@app.route('/api/reportes/clientes-mas-maquinas', methods=['GET'])
def get_clientes_mas_maquinas():
    resultado = reporte_clientes_con_mas_maquinas()
    return jsonify(resultado)


# === MAIN SERVER ===
if __name__ == '__main__':
    app.run(debug=True)
