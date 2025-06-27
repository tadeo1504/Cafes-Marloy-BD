# archivo: app.py
# python -m backend.app

#importar flask y otros módulos necesarios
from flask import Flask, request, jsonify
from flask_cors import CORS  # para permitir acceso desde el frontend

# importar las funciones de conexión a la base de datos y las consultas
from backend.db.conexion import crear_conexion, cerrar_conexion
from backend.db.queries.clientes_queries import insertar_cliente, editar_cliente, eliminar_cliente, mostrar_clientes
from backend.controllers.auth_controller import login_usuario, registrar_usuario
from backend.controllers.proveedores_controller import insertar_proveedor, editar_proveedor, eliminar_proveedor, mostrar_proveedores
from backend.controllers.insumos_controller import insertar_insumo, editar_insumo, eliminar_insumo, mostrar_insumos
from backend.controllers.mantenimientos_controller import insertar_mantenimiento, editar_mantenimiento, eliminar_mantenimiento, mostrar_mantenimientos
from backend.controllers.maquinas_controller import insertar_maquina, editar_maquina, eliminar_maquina, mostrar_maquinas
from backend.controllers.tecnicos_controller import insertar_tecnico, editar_tecnico, eliminar_tecnico, mostrar_tecnicos

# importar el decorador de autenticación
from backend.auth.decorators import solo_admin  # importar el decorador


app = Flask(__name__)
CORS(app)  # permite peticiones desde el navegador

# === CLIENTES ===

@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    clientes = mostrar_clientes(conexion)
    cerrar_conexion(conexion)

    return jsonify(clientes)


@app.route('/api/clientes', methods=['POST'])
def post_cliente():
    data = request.json
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
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = editar_cliente(
        conexion,
        data.get("nombre"),
        data.get("direccion"),
        data.get("telefono"),
        data.get("correo"),
        id
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

    exito = eliminar_cliente(conexion, (id,))
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Cliente eliminado correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo eliminar el cliente"}), 400


# === PROVEEDORES ===
@app.route('/api/proveedores', methods=['GET'])
@solo_admin  # solo los administradores pueden acceder a esta ruta
def get_proveedores():
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    proveedores = mostrar_proveedores(conexion)
    cerrar_conexion(conexion)

    return jsonify(proveedores)

@app.route('/api/proveedores', methods=['POST'])
@solo_admin  # solo los administradores pueden acceder a esta ruta
def post_proveedor():
    data = request.json
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = insertar_proveedor(
        conexion,
        data.get("nombre"),
        data.get("direccion"),
        data.get("telefono"),
        data.get("correo")
    )
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Proveedor insertado correctamente"}), 201
    return jsonify({"ok": False, "mensaje": "No se pudo insertar el proveedor"}), 400

@app.route('/api/proveedores/<int:id>', methods=['PUT'])
@solo_admin  # solo los administradores pueden acceder a esta ruta
def put_proveedor(id):
    data = request.json
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = editar_proveedor(
        conexion,
        data.get("nombre"),
        data.get("direccion"),
        data.get("telefono"),
        data.get("correo"),
        id
    )
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Proveedor modificado correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo modificar el proveedor"}), 400

@app.route('/api/proveedores/<int:id>', methods=['DELETE'])
@solo_admin  # solo los administradores pueden acceder a esta ruta
def delete_proveedor(id):
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = eliminar_proveedor(conexion, (id,))
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Proveedor eliminado correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo eliminar el proveedor"}), 400

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
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = insertar_insumo(
        conexion,
        data.get("nombre"),
        data.get("descripcion"),
        data.get("cantidad"),
        data.get("precio")
    )
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Insumo insertado correctamente"}), 201
    return jsonify({"ok": False, "mensaje": "No se pudo insertar el insumo"}), 400

@app.route('/api/insumos/<int:id>', methods=['PUT'])
def put_insumo(id):
    data = request.json
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = editar_insumo(
        conexion,
        data.get("nombre"),
        data.get("descripcion"),
        data.get("cantidad"),
        data.get("precio"),
        id
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

    exito = eliminar_insumo(conexion, (id,))
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
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = insertar_mantenimiento(
        conexion,
        data.get("fecha"),
        data.get("descripcion"),
        data.get("costo"),
        data.get("proveedor_id")
    )
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Mantenimiento insertado correctamente"}), 201
    return jsonify({"ok": False, "mensaje": "No se pudo insertar el mantenimiento"}), 400

@app.route('/api/mantenimientos/<int:id>', methods=['PUT'])
def put_mantenimiento(id):
    data = request.json
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = editar_mantenimiento(
        conexion,
        data.get("fecha"),
        data.get("descripcion"),
        data.get("costo"),
        data.get("proveedor_id"),
        id
    )
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Mantenimiento modificado correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo modificar el mantenimiento"}), 400

@app.route('/api/mantenimientos/<int:id>', methods=['DELETE'])
def delete_mantenimiento(id):
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = eliminar_mantenimiento(conexion, (id,))
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Mantenimiento eliminado correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo eliminar el mantenimiento"}), 400

# === MAQUINAS ===
@app.route('/api/maquinas', methods=['GET'])
@solo_admin  # solo los administradores pueden acceder a esta ruta
def get_maquinas():
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    maquinas = mostrar_maquinas(conexion)
    cerrar_conexion(conexion)

    return jsonify(maquinas)

@app.route('/api/maquinas', methods=['POST'])
@solo_admin  # solo los administradores pueden acceder a esta ruta
def post_maquina():
    data = request.json
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = insertar_maquina(
        conexion,
        data.get("nombre"),
        data.get("descripcion"),
        data.get("costo"),
        data.get("proveedor_id")
    )
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Máquina insertada correctamente"}), 201
    return jsonify({"ok": False, "mensaje": "No se pudo insertar la máquina"}), 400

@app.route('/api/maquinas/<int:id>', methods=['PUT'])
@solo_admin  # solo los administradores pueden acceder a esta ruta
def put_maquina(id):
    data = request.json
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = editar_maquina(
        conexion,
        data.get("nombre"),
        data.get("descripcion"),
        data.get("costo"),
        data.get("proveedor_id"),
        id
    )
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Máquina modificada correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo modificar la máquina"}), 400

@app.route('/api/maquinas/<int:id>', methods=['DELETE'])
@solo_admin  # solo los administradores pueden acceder a esta ruta
def delete_maquina(id):
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = eliminar_maquina(conexion, (id,))
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Máquina eliminada correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo eliminar la máquina"}), 400

# === TÉCNICOS ===
@app.route('/api/tecnicos', methods=['GET'])
@solo_admin  # solo los administradores pueden acceder a esta ruta
def get_tecnicos():
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    tecnicos = mostrar_tecnicos(conexion)
    cerrar_conexion(conexion)

    return jsonify(tecnicos)

@app.route('/api/tecnicos', methods=['POST'])
@solo_admin  # solo los administradores pueden acceder a esta ruta
def post_tecnico():
    data = request.json
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = insertar_tecnico(
        conexion,
        data.get("nombre"),
        data.get("apellido"),
        data.get("telefono"),
        data.get("correo")
    )
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Técnico insertado correctamente"}), 201
    return jsonify({"ok": False, "mensaje": "No se pudo insertar el técnico"}), 400

@app.route('/api/tecnicos/<int:id>', methods=['PUT'])
@solo_admin  # solo los administradores pueden acceder a esta ruta
def put_tecnico(id):
    data = request.json
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = editar_tecnico(
        conexion,
        data.get("nombre"),
        data.get("apellido"),
        data.get("telefono"),
        data.get("correo"),
        id
    )
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Técnico modificado correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo modificar el técnico"}), 400

@app.route('/api/tecnicos/<int:id>', methods=['DELETE'])
@solo_admin  # solo los administradores pueden acceder a esta ruta
def delete_tecnico(id):
    conexion = crear_conexion()
    if not conexion:
        return jsonify({"ok": False, "mensaje": "Error de conexión"}), 500

    exito = eliminar_tecnico(conexion, (id,))
    cerrar_conexion(conexion)
    if exito:
        return jsonify({"ok": True, "mensaje": "Técnico eliminado correctamente"})
    return jsonify({"ok": False, "mensaje": "No se pudo eliminar el técnico"}), 400


# === AUTENTICACIÓN (básico) ===

@app.route('/api/usuarios/login', methods=['POST'])
def login():
    data = request.json
    correo = data.get('correo')
    contrasena = data.get('contrasena')

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

    resultado = registrar_usuario(correo, contrasena)

    if resultado.get("success"):
        return jsonify({"ok": True, "mensaje": "Usuario registrado correctamente"})
    return jsonify({"ok": False, "error": resultado.get("error", "Error al registrar")}), 400


# === MAIN SERVER ===
if __name__ == '__main__':
    app.run(debug=True)
