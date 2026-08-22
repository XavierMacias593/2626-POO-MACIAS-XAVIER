class Producto:
    """Representa un producto disponible en el restaurante."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        if not codigo.strip() or not nombre.strip() or not categoria.strip():
            raise ValueError("El código, nombre y categoría son obligatorios.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        self.codigo = codigo.strip()
        self.nombre = nombre.strip()
        self.categoria = categoria.strip()
        self.precio = float(precio)

    def to_dict(self) -> dict[str, str | float]:
        """Convierte el producto en un registro compatible con JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
        }

    def mostrar_informacion(self) -> str:
        return (
            f"[{self.codigo}] {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: ${self.precio:.2f}"
        )
