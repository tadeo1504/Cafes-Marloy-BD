#aca estara el main que se podria ejecutar si no hubiese un servidor web
#hara todo por consola

import sys
from backend.controllers.clientes_controller import (
    alta_cliente,
    modificar_cliente,
    baja_cliente,
    mostrar_clientes
)
from backend.db.conexion import crear_conexion, cerrar_conexion

def main():
    print("Esta es la aplicacion de gestion de cafes desde la consola")
    while True:
        
        print("\nOpciones:")
        print("1. Alta de Cliente")
        print("2. Modificación de Cliente")
        print("3. Baja de Cliente")
        print("4. Mostrar Clientes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            alta_cliente()
        elif opcion == '2':
            modificar_cliente()
        elif opcion == '3':
            baja_cliente()
        elif opcion == '4':
            mostrar_clientes()
        elif opcion == '5':
            print("Saliendo...")
            sys.exit(0)
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
