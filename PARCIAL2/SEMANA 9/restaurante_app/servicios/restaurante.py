from __future__ import annotations

from typing import Optional

from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    """Servicio encargado de administrar productos y usuarios del restaurante."""

    def __init__(self) -> None:
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self.opciones_menu: tuple[str, ...] = (
            "1. Registrar producto",
            "2. Buscar producto",
            "3. Actualizar producto",
            "4. Eliminar producto",
            "5. Listar productos",
            "6. Registrar usuario",
            "7. Listar usuarios",
            "8. Mostrar categorías",
            "9. Salir",
        )
        self.acciones_menu: dict[str, str] = {
            "1": "registrar_producto",
            "2": "buscar_producto",
            "3": "actualizar_producto",
            "4": "eliminar_producto",
            "5": "listar_productos",
            "6": "registrar_usuario",
            "7": "listar_usuarios",
            "8": "mostrar_categorias",
            "9": "salir",
        }

    def registrar_producto(self, producto: Producto) -> bool:
        if any(p.codigo == producto.codigo for p in self.productos):
            return False
        self.productos.append(producto)
        return True

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: Optional[str] = None,
        categoria: Optional[str] = None,
        precio: Optional[float] = None,
    ) -> bool:
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is None:
            return False

        if nombre is not None:
            producto.nombre = nombre
        if categoria is not None:
            producto.categoria = categoria
        if precio is not None:
            producto.precio = precio
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
        if any(u.identificacion == usuario.identificacion for u in self.usuarios):
            return False
        self.usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios

    def mostrar_categorias(self) -> set[str]:
        categorias: set[str] = set()
        for producto in self.productos:
            categorias.add(producto.categoria)
        return categorias
