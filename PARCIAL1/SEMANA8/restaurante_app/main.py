from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")

def registrar_producto(servicio: Restaurante):
    print("\n--- Registrar Producto ---")
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría del producto: ")
    try:
        precio = float(input("Ingrese el precio: "))
        producto = Producto(codigo, nombre, categoria, precio)
        if servicio.registrar_producto(producto):
            print("Producto registrado correctamente.")
        else:
            print("Error: Ya existe un producto con ese código.")
    except ValueError:
        print("Error: El precio debe ser un número válido.")

def registrar_bebida(servicio: Restaurante):
    print("\n--- Registrar Bebida ---")
    codigo = input("Ingrese el código de la bebida: ")
    nombre = input("Ingrese el nombre de la bebida: ")
    categoria = input("Ingrese la categoría de la bebida: ")
    try:
        precio = float(input("Ingrese el precio: "))
        tamano = input("Ingrese el tamaño (ej. 500ml, 1L): ")
        tipo_envase = input("Ingrese el tipo de envase (ej. Botella, Lata): ")
        bebida = Bebida(codigo, nombre, categoria, precio, tamano, tipo_envase)
        if servicio.registrar_producto(bebida):
            print("Bebida registrada correctamente.")
        else:
            print("Error: Ya existe un producto con ese código.")
    except ValueError:
        print("Error: El precio debe ser un número válido.")

def registrar_cliente(servicio: Restaurante):
    print("\n--- Registrar Cliente ---")
    identificacion = input("Ingrese la identificación del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    correo = input("Ingrese el correo del cliente: ")
    cliente = Cliente(identificacion, nombre, correo)
    if servicio.registrar_cliente(cliente):
        print("Cliente registrado correctamente.")
    else:
        print("Error: Ya existe un cliente con esa identificación.")

def principal():
    restaurante_servicio = Restaurante()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_producto(restaurante_servicio)
        elif opcion == "2":
            registrar_bebida(restaurante_servicio)
        elif opcion == "3":
            registrar_cliente(restaurante_servicio)
        elif opcion == "4":
            print("\n")
            restaurante_servicio.listar_productos()
        elif opcion == "5":
            print("\n")
            restaurante_servicio.listar_clientes()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    principal()
