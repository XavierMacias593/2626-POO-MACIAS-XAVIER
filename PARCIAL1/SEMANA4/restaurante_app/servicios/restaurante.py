from typing import Optional

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
        for indice, producto in enumerate(self.productos, start=1):
            print(f"  {indice}. {producto}")

    def listar_clientes(self) -> None:
        """Muestra en consola la lista de clientes registrados."""
        print(f"Clientes registrados en {self.nombre}:")
        if not self.clientes:
            print("  (sin clientes)")
            return
        for indice, cliente in enumerate(self.clientes, start=1):
            print(f"  {indice}. {cliente}")

    def buscar_producto(self, nombre: str) -> Optional[Producto]:
        """Busca un producto por nombre usando coincidencia parcial."""
        nombre_minusculo = nombre.lower()
        for producto in self.productos:
            if nombre_minusculo in producto.nombre.lower():
                return producto
        return None

    def buscar_cliente(self, nombre: str) -> Optional[Cliente]:
        """Busca un cliente por nombre usando coincidencia parcial."""
        nombre_minusculo = nombre.lower()
        for cliente in self.clientes:
            if nombre_minusculo in cliente.nombre.lower():
                return cliente
        return None

    def mostrar_resumen(self) -> None:
        """Muestra un resumen organizado del estado actual del restaurante."""
        print("-" * 50)
        print(f"Resumen del restaurante: {self.nombre}")
        print(f"Total productos: {len(self.productos)}")
        print(f"Total clientes: {len(self.clientes)}")
        print("-" * 50)
        self.listar_productos()
        print()
        self.listar_clientes()
        print("-" * 50)
