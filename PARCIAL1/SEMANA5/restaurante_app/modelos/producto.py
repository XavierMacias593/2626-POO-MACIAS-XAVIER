# Clase que representa un producto disponible en el restaurante.
class Producto:
    def __init__(self, nombre: str, precio: float, categoria: str, descripcion: str = "", stock: int = 0, disponible: bool = True):
        """Inicializa un producto con datos básicos y estado de disponibilidad."""
        self.nombre = nombre
        self.precio = float(precio)
        self.categoria = categoria
        self.descripcion = descripcion
        self.stock = int(stock)
        self.disponible = bool(disponible)

    def aplicar_descuento(self, porcentaje: float) -> None:
        """Aplica un descuento al precio del producto."""
        if porcentaje <= 0 or porcentaje >= 100:
            return
        descuento = self.precio * (porcentaje / 100.0)
        self.precio = round(self.precio - descuento, 2)

    def actualizar_stock(self, cantidad: int) -> None:
        """Modifica el stock del producto sin permitir valores negativos."""
        self.stock += cantidad
        if self.stock < 0:
            self.stock = 0

    def mostrar_estado(self) -> str:
        """Devuelve un resumen del estado del producto."""
        estado = "Disponible" if self.disponible else "Agotado"
        return f"{self.nombre} | Stock: {self.stock} | Estado: {estado}"

    def formatear_precio(self) -> str:
        return f"${self.precio:.2f}"

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "Agotado"
        return f"{self.nombre} ({self.categoria}) - {self.formatear_precio()} | Stock: {self.stock} | {estado}"
