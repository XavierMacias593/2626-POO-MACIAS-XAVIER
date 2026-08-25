class Venta:
    """Representa la relación entre un usuario y un producto vendido."""

    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int) -> None:
        if not usuario_id.strip() or not producto_codigo.strip():
            raise ValueError("El usuario y el producto son obligatorios.")
        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero mayor que cero.")
        self.usuario_id = usuario_id.strip()
        self.producto_codigo = producto_codigo.strip()
        self.cantidad = cantidad

    def to_dict(self) -> dict[str, str | int]:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
        }
