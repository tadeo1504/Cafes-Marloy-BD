#aca estara el main que se podria ejecutar si no hubiese un servidor web
#hara todo por consola

from getpass import getpass  # para ocultar la contraseña en consola
import sys
from backend.controllers.auth_controller import (
    login_usuario,
    registrar_usuario
)
from backend.controllers.clientes_controller import (
    alta_cliente,
    modificar_cliente,
    baja_cliente,
    mostrar_clientes
)
 from backend.controllers.insumos_controller import (
    alta_insumo,
    modificar_insumo,
    baja_insumo,
    mostrar_insumos
 )
 from backend.controllers.proveedores_controller import (
    alta_proveedor,
    modificar_proveedor,
    baja_proveedor,
    mostrar_proveedores
 )
from backend.controllers.mantenimientos_controller import (
    alta_mantenimiento,
    modificar_mantenimiento,
    baja_mantenimiento,
    mostrar_mantenimientos
)
from backend.controllers. maquinas_controller import (
    alta_maquina,
    modificar_maquina,
    baja_maquina,
    # mostrar_maquinas
)
from backend.controllers.tecnicos_controller import (
    alta_tecnico,
    modificar_tecnico,
    baja_tecnico,
    # mostrar_tecnicos
)


def menu_principal():
    """Menú con los distintos ABM. Asume que el usuario YA está logueado."""
    while True:
        print("\n=== Menú Principal ===")
        print("1. Clientes")
        print("2. Insumos")
        print("3. Proveedores")
        print("4. Mantenimientos")
        print("5. Máquinas")
        print("6. Técnicos")
        print("7. Cerrar sesión")

        opcion = input("Seleccione una opción: ").strip()

        if   opcion == '1': menu_clientes()
        elif opcion == '2': menu_insumos()
        elif opcion == '3': menu_proveedores()
        elif opcion == '4': menu_mantenimientos()
        elif opcion == '5': menu_maquinas()
        elif opcion == '6': menu_tecnicos()
        elif opcion == '7':
            print("Cerrando sesión…\n")
            break
        else:
            print("Opción no válida, intente nuevamente.")


def flujo_login():
    """Bucle que pide usuario y contraseña hasta que inicie sesión correctamente o elija salir."""
    while True:
        print("\n=== Inicio de Sesión ===")
        correo = input("Usuario: ").strip()
        contrasena = input("Contraseña: ")

        resultado = login_usuario(correo, contrasena)

        if resultado.get('success'):
            print(f"\n✅ Bienvenido, {correo}.\n")
            return resultado['usuario']  # o también podés retornar el token si lo usás
        else:
            print(f"❌ {resultado.get('error', 'Error desconocido.')}")
            opcion = input("¿Desea intentar nuevamente? (s/n): ").lower().strip()
            if opcion != 's':
                print("Saliendo del sistema.")
                exit()


def main():
    print("=== Sistema de Gestión de Cafés Marloy ===")
    
    usuario_logueado = flujo_login()  # esto te asegura que no se entra sin estar logueado

    # si querés podés usar el usuario_logueado para mostrar nombre, rol, etc.
    menu_principal()  # o lo que sea que venga después del login


# ---- Sub-menús (un ejemplo, los otros siguen el mismo patrón) ----
def menu_clientes():
    while True:
        print("\n=== Menú de Clientes ===")
        print("1. Alta")
        print("2. Modificar")
        print("3. Baja")
        print("4. Listar")
        print("5. Volver")

        op = input("Opción: ").strip()
        if   op == '1': alta_cliente()
        elif op == '2': modificar_cliente()
        elif op == '3': baja_cliente()
        elif op == '4': mostrar_clientes()
        elif op == '5': break
        else: print("Opción no válida.")


def menu_insumos():
    while True:
        print("\n=== Menú de Insumos ===")
        print("1. Alta")
        print("2. Modificar")
        print("3. Baja")
        print("4. Listar")
        print("5. Volver")

        op = input("Opción: ").strip()
        if   op == '1': alta_insumo()
        elif op == '2': modificar_insumo()
        elif op == '3': baja_insumo()
        elif op == '4': mostrar_insumos()
        elif op == '5': break
        else: print("Opción no válida.")

def menu_mantenimientos():
    while True:
        print("\n=== Menú de Mantenimientos ===")
        print("1. Alta")
        print("2. Modificar")
        print("3. Baja")
        print("4. Listar")
        print("5. Volver")

        op = input("Opción: ").strip()
        if   op == '1': alta_mantenimiento()
        elif op == '2': modificar_mantenimiento()
        elif op == '3': baja_mantenimiento()
        elif op == '4': mostrar_mantenimientos()
        elif op == '5': break
        else: print("Opción no válida.")

def menu_maquinas():
    while True:
        print("\n=== Menú de Maquinas ===")
        print("1. Alta")
        print("2. Modificar")
        print("3. Baja")
        print("4. Listar")
        print("5. Volver")

        op = input("Opción: ").strip()
        if   op == '1': alta_maquina()
        elif op == '2': modificar_maquina()
        elif op == '3': baja_maquina()
        elif op == '4': mostrar_maquinas()
        elif op == '5': break
        else: print("Opción no válida.")

def menu_proveedores():
    while True:
        print("\n=== Menú de Proveedores ===")
        print("1. Alta")
        print("2. Modificar")
        print("3. Baja")
        print("4. Listar")
        print("5. Volver")

        op = input("Opción: ").strip()
        if   op == '1': alta_proveedor()
        elif op == '2': modificar_proveedor()
        elif op == '3': baja_proveedor()
        elif op == '4': mostrar_proveedores()
        elif op == '5': break
        else: print("Opción no válida.")

def menu_tecnicos():
    while True:
        print("\n=== Menú de Tecnicos ===")
        print("1. Alta")
        print("2. Modificar")
        print("3. Baja")
        print("4. Listar")
        print("5. Volver")

        op = input("Opción: ").strip()
        if   op == '1': alta_tecnico()
        elif op == '2': modificar_tecnico()
        elif op == '3': baja_tecnico()
        elif op == '4': mostrar_tecnicos()
        elif op == '5': break
        else: print("Opción no válida.")


if __name__ == "__main__":
    main()

