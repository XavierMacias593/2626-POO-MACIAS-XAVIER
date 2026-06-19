# Clase que representa un producto del restaurante (plato, bebida, etc.)
class Producto:
    def __init__(self, nombre: str, precio: float, categoria: str, descripcion: str = ""):
        """Inicializa un producto con nombre, precio, categoría y una descripción opcional."""
        self.nombre = nombre
        self.precio = float(precio)
        self.categoria = categoria
        self.descripcion = descripcion

    def aplicar_descuento(self, porcentaje: float) -> None:
        """Aplica un descuento (porcentaje entre 0 y 100) al precio del producto."""
        if porcentaje <= 0 or porcentaje >= 100:
            return
        descuento = self.precio * (porcentaje / 100.0)
        self.precio = round(self.precio - descuento, 2)

    def formatear_precio(self) -> str:
        return f"${self.precio:.2f}"

    def __str__(self) -> str:
        return f"{self.nombre} ({self.categoria}) - {self.formatear_precio()}\n  {self.descripcion}"
