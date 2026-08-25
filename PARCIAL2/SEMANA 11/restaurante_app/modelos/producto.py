class Producto:
    """Representa un producto disponible en el restaurante."""

    def __init__(
        self, codigo: str, nombre: str, categoria: str, precio: float, stock: int = 0
    ) -> None:
        if not codigo.strip() or not nombre.strip() or not categoria.strip():
            raise ValueError("El código, nombre y categoría son obligatorios.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if isinstance(stock, bool) or not isinstance(stock, int) or stock < 0:
            raise ValueError("El stock debe ser un entero mayor o igual que cero.")

        self.codigo = codigo.strip()
        self.nombre = nombre.strip()
        self.categoria = categoria.strip()
        self.precio = float(precio)
        self.stock = stock

    def vender(self, cantidad: int) -> None:
        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero mayor que cero.")
        if cantidad > self.stock:
            raise ValueError("No hay stock suficiente.")
        self.stock -= cantidad

    def to_dict(self) -> dict[str, str | float | int]:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
        }

    def mostrar_informacion(self) -> str:
        return (
            f"[{self.codigo}] {self.nombre} | Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | Stock: {self.stock}"
        )
