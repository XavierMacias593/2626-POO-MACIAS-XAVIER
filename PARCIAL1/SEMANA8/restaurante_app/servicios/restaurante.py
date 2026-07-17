from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self):
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    def registrar_producto(self, producto: Producto) -> bool:
        for p in self.productos:
            if p.codigo == producto.codigo:
                return False
        self.productos.append(producto)
        return True

    def registrar_cliente(self, cliente: Cliente) -> bool:
        for c in self.clientes:
            if c.identificacion == cliente.identificacion:
                return False
        self.clientes.append(cliente)
        return True

    def listar_productos(self) -> None:
        if not self.productos:
            print("No hay productos registrados.")
        else:
            print("--- LISTA DE PRODUCTOS Y BEBIDAS ---")
            for producto in self.productos:
                print(producto.mostrar_informacion())

    def listar_clientes(self) -> None:
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            print("--- LISTA DE CLIENTES ---")
            for cliente in self.clientes:
                print(cliente.mostrar_informacion())
