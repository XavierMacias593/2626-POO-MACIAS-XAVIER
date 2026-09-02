from __future__ import annotations

from typing import Optional

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:
    """Administra las colecciones y reglas de negocio del restaurante."""

    def __init__(self) -> None:
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []
        self._productos_por_codigo: dict[str, Producto] = {}
        self._usuarios_por_identificacion: dict[str, Usuario] = {}
        self._ventas_por_usuario: dict[str, list[Venta]] = {}
        self.opciones_menu: tuple[str, ...] = (
            "1. Registrar producto", "2. Buscar producto", "3. Actualizar producto",
            "4. Eliminar producto", "5. Listar productos", "6. Registrar usuario",
            "7. Listar usuarios", "8. Mostrar categorías", "9. Vender producto",
            "10. Consultar ventas por usuario", "11. Salir",
        )

    def _reconstruir_indices(self) -> None:
        self._productos_por_codigo = {producto.codigo: producto for producto in self._productos}
        self._usuarios_por_identificacion = {usuario.identificacion: usuario for usuario in self._usuarios}
        self._ventas_por_usuario = {}
        for venta in self._ventas:
            self._ventas_por_usuario.setdefault(venta.usuario_id, []).append(venta)

    def registrar_producto(self, producto: Producto) -> bool:
        if producto.codigo in self._productos_por_codigo:
            return False
        self._productos.append(producto)
        self._productos_por_codigo[producto.codigo] = producto
        return True

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        return self._productos_por_codigo.get(codigo)

    def actualizar_producto(
        self, codigo: str, nombre: Optional[str] = None, categoria: Optional[str] = None,
        precio: Optional[float] = None, stock: Optional[int] = None,
    ) -> bool:
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is None:
            return False
        try:
            producto_validado = Producto(
                codigo, nombre if nombre is not None else producto.nombre,
                categoria if categoria is not None else producto.categoria,
                precio if precio is not None else producto.precio,
                stock if stock is not None else producto.stock,
            )
        except (TypeError, ValueError):
            return False
        producto.nombre = producto_validado.nombre
        producto.categoria = producto_validado.categoria
        producto.precio = producto_validado.precio
        producto.stock = producto_validado.stock
        self._productos_por_codigo[codigo] = producto
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is None:
            return False
        self._productos.remove(producto)
        self._productos_por_codigo.pop(codigo, None)
        return True

    def listar_productos(self) -> list[Producto]:
        return self._productos

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if usuario.identificacion in self._usuarios_por_identificacion:
            return False
        self._usuarios.append(usuario)
        self._usuarios_por_identificacion[usuario.identificacion] = usuario
        return True

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        return self._usuarios_por_identificacion.get(identificacion)

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios

    def registrar_venta(self, venta: Venta) -> bool:
        if self.buscar_usuario(venta.usuario_id) is None:
            return False
        producto = self.buscar_producto_por_codigo(venta.producto_codigo)
        if producto is None or venta.cantidad > producto.stock:
            return False
        producto.vender(venta.cantidad)
        self._ventas.append(venta)
        self._ventas_por_usuario.setdefault(venta.usuario_id, []).append(venta)
        return True

    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto_por_codigo(codigo_producto)
        if usuario is None or producto is None:
            return False
        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
            return False
        if producto.stock < cantidad:
            return False
        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        producto.vender(cantidad)
        self._ventas.append(venta)
        self._ventas_por_usuario.setdefault(venta.usuario_id, []).append(venta)
        return True

    def listar_ventas(self) -> list[Venta]:
        return self._ventas

    def cargar_venta(self, venta: Venta) -> None:
        self._ventas.append(venta)
        self._ventas_por_usuario.setdefault(venta.usuario_id, []).append(venta)

    def consultar_ventas_usuario(self, identificacion_usuario: str) -> list[Venta]:
        return list(self._ventas_por_usuario.get(identificacion_usuario, []))

    def mostrar_categorias(self) -> set[str]:
        return {producto.categoria for producto in self._productos}
