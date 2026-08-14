from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.usuario import Usuario


def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    for opcion in Restaurante().opciones_menu:
        print(opcion)
    print("----------------------------------------")


def registrar_producto(servicio: Restaurante) -> None:
    print("\n--- Registrar Producto ---")
    try:
        codigo = input("Ingrese el código del producto: ").strip()
        nombre = input("Ingrese el nombre del producto: ").strip()
        categoria = input("Ingrese la categoría del producto: ").strip()
        precio = float(input("Ingrese el precio del producto: "))

        if not codigo or not nombre or not categoria:
            print("Error: Todos los campos son obligatorios.")
            return

        producto = Producto(codigo, nombre, categoria, precio)
        if servicio.registrar_producto(producto):
            print("Producto registrado correctamente.")
        else:
            print("Error: Ya existe un producto con ese código.")
    except ValueError:
        print("Error: El precio debe ser un número válido.")


def buscar_producto(servicio: Restaurante) -> None:
    print("\n--- Buscar Producto ---")
    codigo = input("Ingrese el código del producto a buscar: ").strip()
    producto = servicio.buscar_producto_por_codigo(codigo)
    if producto is None:
        print("No se encontró ningún producto con ese código.")
    else:
        print(producto.mostrar_informacion())


def actualizar_producto(servicio: Restaurante) -> None:
    print("\n--- Actualizar Producto ---")
    codigo = input("Ingrese el código del producto: ").strip()
    producto = servicio.buscar_producto_por_codigo(codigo)
    if producto is None:
        print("No se encontró un producto con ese código.")
        return

    try:
        nuevo_nombre = input(f"Ingrese el nuevo nombre [{producto.nombre}]: ").strip()
        nueva_categoria = input(f"Ingrese la nueva categoría [{producto.categoria}]: ").strip()
        nuevo_precio = input(f"Ingrese el nuevo precio [{producto.precio}]: ").strip()

        nombre_final = nuevo_nombre if nuevo_nombre else producto.nombre
        categoria_final = nueva_categoria if nueva_categoria else producto.categoria
        precio_final = float(nuevo_precio) if nuevo_precio else producto.precio

        if servicio.actualizar_producto(codigo, nombre_final, categoria_final, precio_final):
            print("Producto actualizado correctamente.")
        else:
            print("No fue posible actualizar el producto.")
    except ValueError:
        print("Error: El precio debe ser un valor numérico válido.")


def eliminar_producto(servicio: Restaurante) -> None:
    print("\n--- Eliminar Producto ---")
    codigo = input("Ingrese el código del producto a eliminar: ").strip()
    if servicio.eliminar_producto(codigo):
        print("Producto eliminado correctamente.")
    else:
        print("No existe un producto con ese código.")


def listar_productos(servicio: Restaurante) -> None:
    print("\n--- Listado de Productos ---")
    productos = servicio.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return

    for producto in productos:
        print(producto.mostrar_informacion())


def registrar_usuario(servicio: Restaurante) -> None:
    print("\n--- Registrar Usuario ---")
    try:
        identificacion = input("Ingrese la identificación del usuario: ").strip()
        nombre = input("Ingrese el nombre del usuario: ").strip()
        correo = input("Ingrese el correo del usuario: ").strip()

        if not identificacion or not nombre or not correo:
            print("Error: Los datos del usuario son obligatorios.")
            return

        usuario = Usuario(identificacion, nombre, correo)
        if servicio.registrar_usuario(usuario):
            print("Usuario registrado correctamente.")
        else:
            print("Error: Ya existe un usuario con esa identificación.")
    except ValueError:
        print("Error: Se produjo un problema al registrar el usuario.")


def listar_usuarios(servicio: Restaurante) -> None:
    print("\n--- Listado de Usuarios ---")
    usuarios = servicio.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    for usuario in usuarios:
        print(usuario.mostrar_informacion())


def mostrar_categorias(servicio: Restaurante) -> None:
    print("\n--- Categorías Disponibles ---")
    categorias = servicio.mostrar_categorias()
    if not categorias:
        print("No hay categorías registradas.")
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")


def principal() -> None:
    servicio = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_producto(servicio)
        elif opcion == "2":
            buscar_producto(servicio)
        elif opcion == "3":
            actualizar_producto(servicio)
        elif opcion == "4":
            eliminar_producto(servicio)
        elif opcion == "5":
            listar_productos(servicio)
        elif opcion == "6":
            registrar_usuario(servicio)
        elif opcion == "7":
            listar_usuarios(servicio)
        elif opcion == "8":
            mostrar_categorias(servicio)
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    principal()
