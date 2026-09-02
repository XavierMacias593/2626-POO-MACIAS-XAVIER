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


def guardar_cambios(accion) -> bool:
    try:
        accion()
        return True
    except PermissionError as error:
        print(f"Error de persistencia: {error}")
        return False


def registrar_producto(servicio: Restaurante, archivo: ArchivoServicio) -> None:
    print("\n--- Registrar Producto ---")
    try:
        producto = Producto(
            input("Ingrese el código del producto: "),
            input("Ingrese el nombre del producto: "),
            input("Ingrese la categoría del producto: "),
            float(input("Ingrese el precio del producto: ")),
            int(input("Ingrese el stock inicial: ")),
        )
        if servicio.registrar_producto(producto):
            guardar_cambios(lambda: archivo.guardar_productos(servicio.listar_productos()))
            print("Producto registrado correctamente.")
        else:
            print("Error: ya existe un producto con ese código.")
    except ValueError as error:
        print(f"Error: {error}")


def buscar_producto(servicio: Restaurante) -> None:
    codigo = input("Ingrese el código del producto a buscar: ").strip()
    producto = servicio.buscar_producto_por_codigo(codigo)
    print(producto.mostrar_informacion() if producto else "No se encontró el producto.")


def actualizar_producto(servicio: Restaurante, archivo: ArchivoServicio) -> None:
    codigo = input("Ingrese el código del producto: ").strip()
    producto = servicio.buscar_producto_por_codigo(codigo)
    if producto is None:
        print("No se encontró el producto.")
        return
    try:
        nombre = input(f"Nuevo nombre [{producto.nombre}]: ").strip() or producto.nombre
        categoria = input(f"Nueva categoría [{producto.categoria}]: ").strip() or producto.categoria
        precio_texto = input(f"Nuevo precio [{producto.precio}]: ").strip()
        stock_texto = input(f"Nuevo stock [{producto.stock}]: ").strip()
        actualizado = servicio.actualizar_producto(
            codigo, nombre, categoria,
            float(precio_texto) if precio_texto else producto.precio,
            int(stock_texto) if stock_texto else producto.stock,
        )
        if actualizado:
            guardar_cambios(lambda: archivo.guardar_productos(servicio.listar_productos()))
            print("Producto actualizado correctamente.")
        else:
            print("Error: los datos no son válidos.")
    except ValueError as error:
        print(f"Error: {error}")


def eliminar_producto(servicio: Restaurante, archivo: ArchivoServicio) -> None:
    codigo = input("Ingrese el código del producto a eliminar: ").strip()
    if servicio.eliminar_producto(codigo):
        guardar_cambios(lambda: archivo.guardar_productos(servicio.listar_productos()))
        print("Producto eliminado correctamente.")
    else:
        print("No existe un producto con ese código.")


def listar_productos(servicio: Restaurante) -> None:
    productos = servicio.listar_productos()
    print("\n".join(producto.mostrar_informacion() for producto in productos) or "No hay productos registrados.")


def registrar_usuario(servicio: Restaurante, archivo: ArchivoServicio) -> None:
    print("\n--- Registrar Usuario ---")
    try:
        usuario = Usuario(
            input("Ingrese la identificación: "),
            input("Ingrese el nombre: "),
            input("Ingrese el correo: "),
        )
        if servicio.registrar_usuario(usuario):
            guardar_cambios(lambda: archivo.guardar_usuarios(servicio.listar_usuarios()))
            print("Usuario registrado correctamente.")
        else:
            print("Error: ya existe un usuario con esa identificación.")
    except ValueError as error:
        print(f"Error: {error}")


def listar_usuarios(servicio: Restaurante) -> None:
    usuarios = servicio.listar_usuarios()
    print("\n".join(usuario.mostrar_informacion() for usuario in usuarios) or "No hay usuarios registrados.")


def mostrar_categorias(servicio: Restaurante) -> None:
    categorias = servicio.mostrar_categorias()
    print("\n".join(sorted(categorias)) if categorias else "No hay categorías registradas.")


def vender_producto(servicio: Restaurante, archivo: ArchivoServicio) -> None:
    print("\n--- Vender Producto ---")
    try:
        codigo = input("Ingrese el código del producto: ").strip()
        identificacion = input("Ingrese la identificación del usuario: ").strip()
        cantidad = int(input("Ingrese la cantidad: "))
        if servicio.vender_producto(codigo, identificacion, cantidad):
            guardado = guardar_cambios(
                lambda: (
                    archivo.guardar_productos(servicio.listar_productos()),
                    archivo.guardar_ventas(servicio.listar_ventas()),
                )
            )
            print("Venta registrada correctamente." if guardado else "Venta realizada, pero no se pudo guardar.")
        else:
            print("Venta rechazada: revise usuario, producto, cantidad y stock disponible.")
    except ValueError as error:
        print(f"Error: {error}")


def consultar_ventas(servicio: Restaurante) -> None:
    identificacion = input("Ingrese la identificación del usuario: ").strip()
    ventas = servicio.consultar_ventas_usuario(identificacion)
    if not ventas:
        print("No hay ventas para ese usuario.")
        return
    for venta in ventas:
        producto = servicio.buscar_producto_por_codigo(venta.producto_codigo)
        nombre = producto.nombre if producto else "Producto no disponible"
        print(f"Producto: {nombre} ({venta.producto_codigo}) | Cantidad: {venta.cantidad}")


def principal() -> None:
    servicio = Restaurante()
    archivo = ArchivoServicio()
    for producto in archivo.cargar_productos():
        servicio.registrar_producto(producto)
    for usuario in archivo.cargar_usuarios():
        servicio.registrar_usuario(usuario)
    for venta in archivo.cargar_ventas():
        servicio.cargar_venta(venta)
    servicio._reconstruir_indices()

    acciones = {
        "1": lambda: registrar_producto(servicio, archivo),
        "2": lambda: buscar_producto(servicio),
        "3": lambda: actualizar_producto(servicio, archivo),
        "4": lambda: eliminar_producto(servicio, archivo),
        "5": lambda: listar_productos(servicio),
        "6": lambda: registrar_usuario(servicio, archivo),
        "7": lambda: listar_usuarios(servicio),
        "8": lambda: mostrar_categorias(servicio),
        "9": lambda: vender_producto(servicio, archivo),
        "10": lambda: consultar_ventas(servicio),
    }
    while True:
        mostrar_menu(servicio)
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "11":
            print("Saliendo del sistema...")
            break
        accion = acciones.get(opcion)
        if accion is None:
            print("Opción no válida. Intente nuevamente.")
        else:
            accion()


if __name__ == "__main__":
    principal()
