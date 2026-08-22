from __future__ import annotations

from typing import Optional

from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    """Servicio encargado de administrar productos y usuarios."""

    def __init__(self) -> None:
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self.opciones_menu: tuple[str, ...] = (
            "1. Registrar producto", "2. Buscar producto", "3. Actualizar producto",
            "4. Eliminar producto", "5. Listar productos", "6. Registrar usuario",
            "7. Listar usuarios", "8. Mostrar categorías", "9. Salir",
        )

    def registrar_producto(self, producto: Producto) -> bool:
        if any(item.codigo == producto.codigo for item in self.productos):
            return False
        self.productos.append(producto)
        return True

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        return next((producto for producto in self.productos if producto.codigo == codigo), None)

    def actualizar_producto(
        self, codigo: str, nombre: Optional[str] = None,
        categoria: Optional[str] = None, precio: Optional[float] = None,
    ) -> bool:
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is None:
            return False
        try:
            producto_validado = Producto(
                codigo,
                nombre if nombre is not None else producto.nombre,
                categoria if categoria is not None else producto.categoria,
                precio if precio is not None else producto.precio,
            )
        except (TypeError, ValueError):
            return False
        producto.nombre = producto_validado.nombre
        producto.categoria = producto_validado.categoria
        producto.precio = producto_validado.precio
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is None:
            return False
        self.productos.remove(producto)
        return True

    def listar_productos(self) -> list[Producto]:
        return self.productos

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if any(item.identificacion == usuario.identificacion for item in self.usuarios):
            return False
        self.usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios

    def mostrar_categorias(self) -> set[str]:
        return {producto.categoria for producto in self.productos}
