# Clase que representa a un cliente del restaurante
class Cliente:
    def __init__(self, nombre: str, telefono: str = None, email: str = None):
        """Inicializa un cliente con nombre y datos de contacto opcionales."""
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def actualizar_contacto(self, telefono: str = None, email: str = None) -> None:
        """Actualiza los datos de contacto del cliente."""
        if telefono:
            self.telefono = telefono
        if email:
            self.email = email

    def __str__(self) -> str:
        partes = [f"Nombre: {self.nombre}"]
        if self.telefono:
            partes.append(f"Tel: {self.telefono}")
        if self.email:
            partes.append(f"Email: {self.email}")
        return " | ".join(partes)
