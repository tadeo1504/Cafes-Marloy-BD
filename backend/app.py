# archivo: app.py
# python -m backend.app

from flask import Flask, request, jsonify
from flask_cors import CORS  # para permitir acceso desde el frontend

from backend.db.conexion import crear_conexion, cerrar_conexion
from backend.db.queries.clientes_queries import insertar_cliente, editar_cliente, eliminar_cliente, mostrar_clientes
from backend.controllers.auth_controller import login_usuario, registrar_usuario

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
