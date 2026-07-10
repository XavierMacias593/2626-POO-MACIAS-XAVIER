class Producto:
    """Representa un producto disponible en el restaurante."""

    def __init__(self, nombre, categoria, precio, disponible=True):
        self._nombre = ""
        self._categoria = ""
        self._precio = 0.0
        self._disponible = True

        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor.strip().title()

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        self._categoria = valor.strip().title()

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        try:
            precio_numero = float(valor)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser un número válido.")

        if precio_numero <= 0:
            raise ValueError("El precio del producto debe ser mayor que cero.")

        self._precio = round(precio_numero, 2)

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        if isinstance(valor, str):
            valor = valor.strip().lower() in {"si", "sí", "s", "true", "1", "yes", "y"}

        if not isinstance(valor, bool):
            raise ValueError("La disponibilidad debe ser un valor verdadero o falso.")

        self._disponible = valor

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return (
            f"Nombre: {self.nombre} | Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | Estado: {estado}"
        )
