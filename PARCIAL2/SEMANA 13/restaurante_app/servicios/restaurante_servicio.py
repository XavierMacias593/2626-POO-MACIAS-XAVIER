from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """Gestiona los datos del restaurante y la validación de acceso."""

    def __init__(self, archivo_servicio: ArchivoServicio | None = None) -> None:
        self.archivo_servicio = archivo_servicio or ArchivoServicio()
        self.productos = self.archivo_servicio.cargar_productos()
        self.usuarios = self.archivo_servicio.cargar_usuarios()

    def validar_acceso(self, usuario: str, password: str) -> bool:
        for usuario_registrado in self.usuarios:
            if usuario_registrado.identificacion == usuario and usuario_registrado.password == password:
                return True
        return False

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios

    def listar_productos(self) -> list[Producto]:
        return self.productos

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

    def buscar_producto(self, codigo: str) -> Producto | None:
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def consultar_stock(self, codigo: str) -> int:
        producto = self.buscar_producto(codigo)
        return producto.stock if producto else 0
