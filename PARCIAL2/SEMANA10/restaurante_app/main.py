from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante


def mostrar_menu(servicio: Restaurante) -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    for opcion in servicio.opciones_menu:
        print(opcion)
    print("----------------------------------------")


def guardar_productos(servicio: Restaurante, archivo: ArchivoServicio) -> None:
    try:
        archivo.guardar_productos(servicio.listar_productos())
    except PermissionError as error:
        print(f"Error de persistencia: {error}")


def registrar_producto(servicio: Restaurante, archivo: ArchivoServicio) -> None:
    print("\n--- Registrar Producto ---")
    try:
        codigo = input("Ingrese el código del producto: ").strip()
        nombre = input("Ingrese el nombre del producto: ").strip()
        categoria = input("Ingrese la categoría del producto: ").strip()
        precio = float(input("Ingrese el precio del producto: "))
        producto = Producto(codigo, nombre, categoria, precio)
        if servicio.registrar_producto(producto):
            guardar_productos(servicio, archivo)
            print("Producto registrado correctamente.")
        else:
            print("Error: Ya existe un producto con ese código.")
    except ValueError as error:
        print(f"Error: {error}")


def buscar_producto(servicio: Restaurante) -> None:
    print("\n--- Buscar Producto ---")
    codigo = input("Ingrese el código del producto a buscar: ").strip()
    producto = servicio.buscar_producto_por_codigo(codigo)
    print(producto.mostrar_informacion() if producto else "No se encontró ningún producto con ese código.")


def actualizar_producto(servicio: Restaurante, archivo: ArchivoServicio) -> None:
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
        actualizado = servicio.actualizar_producto(
            codigo,
            nuevo_nombre or producto.nombre,
            nueva_categoria or producto.categoria,
            float(nuevo_precio) if nuevo_precio else producto.precio,
        )
        if actualizado:
            guardar_productos(servicio, archivo)
            print("Producto actualizado correctamente.")
        else:
            print("Error: los datos del producto no son válidos.")
    except ValueError as error:
        print(f"Error: {error}")


def eliminar_producto(servicio: Restaurante, archivo: ArchivoServicio) -> None:
    print("\n--- Eliminar Producto ---")
    codigo = input("Ingrese el código del producto a eliminar: ").strip()
    if servicio.eliminar_producto(codigo):
        guardar_productos(servicio, archivo)
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
        usuario = Usuario(identificacion, nombre, correo)
        print("Usuario registrado correctamente." if servicio.registrar_usuario(usuario) else "Error: Ya existe un usuario con esa identificación.")
    except ValueError as error:
        print(f"Error: {error}")


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
    print("No hay categorías registradas." if not categorias else "\n".join(f"- {categoria}" for categoria in sorted(categorias)))


def principal() -> None:
    servicio = Restaurante()
    archivo = ArchivoServicio()
    for producto in archivo.cargar_productos():
        servicio.registrar_producto(producto)

    acciones = {
        "1": lambda: registrar_producto(servicio, archivo),
        "2": lambda: buscar_producto(servicio),
        "3": lambda: actualizar_producto(servicio, archivo),
        "4": lambda: eliminar_producto(servicio, archivo),
        "5": lambda: listar_productos(servicio),
        "6": lambda: registrar_usuario(servicio),
        "7": lambda: listar_usuarios(servicio),
        "8": lambda: mostrar_categorias(servicio),
    }
    while True:
        mostrar_menu(servicio)
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "9":
            print("Saliendo del sistema...")
            break
        accion = acciones.get(opcion)
        if accion is None:
            print("Opción no válida. Intente nuevamente.")
        else:
            accion()


if __name__ == "__main__":
    principal()
