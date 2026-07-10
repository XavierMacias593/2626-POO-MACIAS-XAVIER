from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Administra los productos y clientes del restaurante."""

    def __init__(self):
        self.productos = []
        self.clientes = []
        self._cargar_datos_ejemplo()

    def _cargar_datos_ejemplo(self):
        """Carga productos y clientes iniciales para mostrar el funcionamiento del sistema."""
        producto_uno = Producto("Hamburguesa", "Comida", 8.50, True)
        producto_dos = Producto("Jugo Natural", "Bebida", 4.25, True)
        cliente_uno = Cliente("Ana Gómez", "ana@example.com", 101)
        cliente_dos = Cliente("Luis Pérez", "luis@example.com", 102)

        self.productos.extend([producto_uno, producto_dos])
        self.clientes.extend([cliente_uno, cliente_dos])

    def mostrar_datos_ejemplo(self):
        """Muestra información inicial de ejemplo del sistema."""
        print("\nDatos de ejemplo cargados al iniciar:")
        for producto in self.productos[:2]:
            print(f"- Producto: {producto.mostrar_informacion()}")
        for cliente in self.clientes[:2]:
            print(f"- Cliente: {cliente.nombre} | {cliente.correo} | ID {cliente.id_cliente}")

    def registrar_producto(self, producto):
        self.productos.append(producto)

    def listar_productos(self):
        return self.productos

    def buscar_productos(self, criterio):
        criterio = criterio.strip().lower()
        if not criterio:
            return []

        return [
            producto
            for producto in self.productos
            if criterio in producto.nombre.lower() or criterio in producto.categoria.lower()
        ]

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        return self.clientes

    def buscar_clientes(self, criterio):
        criterio = criterio.strip().lower()
        if not criterio:
            return []

        return [
            cliente
            for cliente in self.clientes
            if criterio in cliente.nombre.lower()
            or criterio in cliente.correo.lower()
            or criterio == str(cliente.id_cliente)
        ]
