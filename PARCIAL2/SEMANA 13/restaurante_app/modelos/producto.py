class Producto:
    """Representa un producto del restaurante."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> None:
        if not codigo.strip() or not nombre.strip() or not categoria.strip():
            raise ValueError("Código, nombre y categoría son obligatorios.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if isinstance(stock, bool) or not isinstance(stock, int) or stock < 0:
            raise ValueError("El stock debe ser un entero no negativo.")

        self.codigo = codigo.strip()
        self.nombre = nombre.strip()
        self.categoria = categoria.strip()
        self.precio = float(precio)
        self.stock = stock

    def to_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
        }

    def mostrar_informacion(self) -> str:
        return (
            f"[{self.codigo}] {self.nombre} | Categoria: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | Stock: {self.stock}"
        )
