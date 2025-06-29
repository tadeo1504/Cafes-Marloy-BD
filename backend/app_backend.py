#aca estara el main que se podria ejecutar si no hubiese un servidor web
#hara todo por consola
# python -m backend.app_backend

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
    listar_clientes
)
from backend.controllers.insumos_controller import (
    alta_insumo,
    modificar_insumo,
    baja_insumo,
    listar_insumos
 )
from backend.controllers.proveedores_controller import (
    alta_proveedor,
    modificar_proveedor,
    baja_proveedor,
    listar_proveedores
 )
from backend.controllers.mantenimientos_controller import (
    alta_mantenimiento,
    modificar_mantenimiento,
    baja_mantenimiento,
    listar_mantenimientos
)
from backend.controllers. maquinas_controller import (
    alta_maquina,
    modificar_maquina,
    baja_maquina,
    listar_maquinas
)
from backend.controllers.tecnicos_controller import (
    alta_tecnico,
    modificar_tecnico,
    baja_tecnico,
    listar_tecnicos
)
from backend.controllers.registro_consumo_controller import (
    alta_registro_consumo,
    modificar_registro_consumo,
    baja_registro_consumo,
    listar_registros_consumo
)

from backend.controllers.reportes_controller import (
    reporte_total_mensual_por_cliente,
    reporte_insumos_mas_consumidos,
    reporte_tecnicos_mas_mantenimientos,
    reporte_clientes_con_mas_maquinas
)


def menu_principal(usuario):
    """Menú con los distintos ABM. Asume que el usuario YA está logueado."""
    while True:
        print("\n=== Menú Principal ===")
        print("1. Clientes")
        print("2. Insumos")
        print("3. Mantenimientos")
        if usuario.get('es_administrador'):
            print("4. Proveedores")
            print("5. Máquinas")
            print("6. Técnicos")
            print("7. Registros de Consumo")
            print("8. Reportes")

        print("0. Cerrar sesión")

        opcion = input("Seleccione una opción: ").strip()

        if   opcion == '1': menu_clientes()
        elif opcion == '2': menu_insumos()
        elif opcion == '4' and usuario.get('es_administrador'): menu_proveedores()
        elif opcion == '3': menu_mantenimientos()
        elif opcion == '5' and usuario.get('es_administrador'): menu_maquinas()
        elif opcion == '6' and usuario.get('es_administrador'): menu_tecnicos()
        elif opcion == '7' and usuario.get('es_administrador'): menu_registros_consumo()
        elif opcion == '8' and usuario.get('es_administrador'): menu_reportes()
        elif opcion == '0':
            print("Cerrando sesión…\n")
            break
        else:
            print("Opción no válida, intente nuevamente.")


def flujo_login():
    """Bucle que pide correo y contraseña hasta que inicie sesión correctamente o elija salir."""
    while True:
        print("\n=== Inicio de Sesión ===")
        correo = input("Correo: ").strip()
        contrasena = getpass("Contraseña: ")

        resultado = login_usuario(correo, contrasena)

        if resultado.get('success'):
            print(f"\n✅ Bienvenido, {correo}.\n")
            return resultado['usuario'] #aca tambien se guarda si es admin o no
        else:
            print(f"❌ {resultado.get('error', 'Error desconocido.')}")
            opcion = input("¿Desea intentar nuevamente? (s/n): ").lower().strip()
            if opcion != 's':
                print("Saliendo del sistema.")
                exit()

def flujo_registro():
    print("\n=== Registro de Usuario ===")
    correo = input("Correo: ").strip()
    contrasena = getpass("Contraseña: ")
    repetir = getpass("Repetir contraseña: ")

    if contrasena != repetir:
        print("❌ Las contraseñas no coinciden.")
        return

    resultado = registrar_usuario(correo, contrasena) 

    if resultado.get("success"):
        print("✅ Usuario registrado exitosamente.")
    else:
        print(f"❌ {resultado.get('error', 'Error al registrar el usuario.')}")


def main():
    print("=== Sistema de Gestión de Cafés Marloy ===")
    
    while True:
        print("\n1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")

        op = input("Seleccione una opción: ").strip()

        if op == '1':
            usuario_logueado = flujo_login()
            menu_principal(usuario_logueado)
            break
        elif op == '2':
            flujo_registro()
        elif op == '3':
            print("Hasta luego.")
            exit()
        else:
            print("Opción no válida.")


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
        elif op == '4': listar_clientes()
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
        elif op == '4': listar_insumos()
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
        elif op == '4': listar_mantenimientos()
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
        elif op == '4': listar_maquinas()
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
        elif op == '4': listar_proveedores()
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
        elif op == '4': listar_tecnicos()
        elif op == '5': break
        else: print("Opción no válida.")

def menu_registros_consumo():
    while True:
        print("\n=== Menú de Registros de Consumo ===")
        print("1. Alta")
        print("2. Modificar")
        print("3. Baja")
        print("4. Listar")
        print("5. Volver")

        op = input("Opción: ").strip()
        if   op == '1': alta_registro_consumo()
        elif op == '2': modificar_registro_consumo()
        elif op == '3': baja_registro_consumo()
        elif op == '4': listar_registros_consumo()
        elif op == '5': break
        else: print("Opción no válida.")

def menu_reportes():
    while True:
        print("\n=== Menú de Reportes ===")
        print("1. Total mensual a cobrar a cada cliente")
        print("2. Insumos con mayor consumo y costos")
        print("3. Técnicos con más mantenimientos")
        print("4. Clientes con más máquinas instaladas")
        print("5. Volver")

        op = input("Opción: ").strip()

        if op == '1':
            reporte_total_mensual_por_cliente()
        elif op == '2':
            reporte_insumos_mas_consumidos()
        elif op == '3':
            reporte_tecnicos_mas_mantenimientos()
        elif op == '4':
            reporte_clientes_con_mas_maquinas()
        elif op == '5':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()


