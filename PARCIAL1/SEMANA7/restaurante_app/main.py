from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def registrar_producto(restaurante):
    print("\nRegistrar producto")
    nombre = input("Ingrese el nombre del producto: ").strip()
    categoria = input("Ingrese la categoría del producto: ").strip()
    precio = input("Ingrese el precio del producto: ").strip()
    disponible = input("¿Está disponible? (si/no): ").strip().lower()

    try:
        producto = Producto(nombre=nombre, categoria=categoria, precio=precio, disponible=disponible)
        restaurante.registrar_producto(producto)
        print("Producto registrado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")


def listar_productos(restaurante):
    print("\nListado de productos")
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return

    for producto in productos:
        print(producto.mostrar_informacion())


def buscar_producto(restaurante):
    criterio = input("Ingrese el nombre o categoría a buscar: ").strip()
    productos = restaurante.buscar_productos(criterio)
    if not productos:
        print("No se encontraron productos.")
        return

    for producto in productos:
        print(producto.mostrar_informacion())


def registrar_cliente(restaurante):
    print("\nRegistrar cliente")
    nombre = input("Ingrese el nombre del cliente: ").strip()
    correo = input("Ingrese el correo del cliente: ").strip()
    id_cliente = input("Ingrese el identificador del cliente: ").strip()

    try:
        cliente = Cliente(nombre=nombre, correo=correo, id_cliente=int(id_cliente))
        restaurante.registrar_cliente(cliente)
        print("Cliente registrado correctamente.")
    except ValueError:
        print("El identificador debe ser un número entero.")


def listar_clientes(restaurante):
    print("\nListado de clientes")
    clientes = restaurante.listar_clientes()
    if not clientes:
        print("No hay clientes registrados.")
        return

    for cliente in clientes:
        print(f"ID: {cliente.id_cliente} | Nombre: {cliente.nombre} | Correo: {cliente.correo}")


def buscar_cliente(restaurante):
    criterio = input("Ingrese el nombre, correo o ID a buscar: ").strip()
    clientes = restaurante.buscar_clientes(criterio)
    if not clientes:
        print("No se encontraron clientes.")
        return

    for cliente in clientes:
        print(f"ID: {cliente.id_cliente} | Nombre: {cliente.nombre} | Correo: {cliente.correo}")


def mostrar_menu():
    print("=" * 40)
    print("SISTEMA DE RESTAURANTE")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("-" * 40)
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("-" * 40)
    print("7. Salir")


def main():
    restaurante = Restaurante()

    print("=" * 40)
    print("Bienvenido al sistema de restaurante")
    print("=" * 40)
    print("Este programa demuestra cómo los datos ingresados por consola")
    print("se convierten en objetos de Programación Orientada a Objetos.")
    print("Los productos y clientes de ejemplo ya están cargados al iniciar.")
    print("Cuando registres datos nuevos, el sistema creará objetos y los guardará")
    print("en las listas del restaurante para luego listarlos o buscarlos.")
    restaurante.mostrar_datos_ejemplo()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            listar_productos(restaurante)
        elif opcion == "3":
            buscar_producto(restaurante)
        elif opcion == "4":
            registrar_cliente(restaurante)
        elif opcion == "5":
            listar_clientes(restaurante)
        elif opcion == "6":
            buscar_cliente(restaurante)
        elif opcion == "7":
            print("Gracias por usar el sistema del restaurante.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()
