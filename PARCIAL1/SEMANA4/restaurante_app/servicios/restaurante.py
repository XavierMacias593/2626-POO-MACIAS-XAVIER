from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Servicio principal que administra productos y clientes."""

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    def agregar_producto(self, producto: Producto) -> None:
        """Agrega un producto al catálogo del restaurante."""
        self.productos.append(producto)

    def registrar_cliente(self, cliente: Cliente) -> None:
        """Registra un cliente en el sistema."""
        self.clientes.append(cliente)

    def listar_productos(self) -> None:
        """Muestra en consola la lista de productos registrados."""
        print(f"Productos en {self.nombre}:")
        if not self.productos:
            print("  (sin productos)")
            return
        for i, p in enumerate(self.productos, start=1):
            print(f"  {i}. {p}")

    def listar_clientes(self) -> None:
        """Muestra en consola la lista de clientes registrados."""
        print(f"Clientes registrados en {self.nombre}:")
        if not self.clientes:
            print("  (sin clientes)")
            return
        for i, c in enumerate(self.clientes, start=1):
            print(f"  {i}. {c}")

    def buscar_producto(self, nombre: str):
        """Busca un producto por nombre (coincidencia parcial, case-insensitive)."""
        nombre_minus = nombre.lower()
        for p in self.productos:
            if nombre_minus in p.nombre.lower():
                return p
        return None

    def mostrar_resumen(self) -> None:
        """Muestra un resumen organizado del estado actual del restaurante."""
        print("-" * 40)
        print(f"Resumen del restaurante: {self.nombre}")
        print(f"Total productos: {len(self.productos)}")
        print(f"Total clientes: {len(self.clientes)}")
        print("-" * 40)
        self.listar_productos()
        print()
        self.listar_clientes()
        print("-" * 40)
