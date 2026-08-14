class Usuario:
    """Representa a una persona registrada en el sistema del restaurante."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    def mostrar_informacion(self) -> str:
        return f"[{self.identificacion}] {self.nombre} | Correo: {self.correo}"
