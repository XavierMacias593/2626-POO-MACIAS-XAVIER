class Usuario:
    """Representa a una persona registrada en el sistema del restaurante."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        if not identificacion.strip() or not nombre.strip() or not correo.strip():
            raise ValueError("Los datos del usuario son obligatorios.")
        self.identificacion = identificacion.strip()
        self.nombre = nombre.strip()
        self.correo = correo.strip()

    def mostrar_informacion(self) -> str:
        return f"[{self.identificacion}] {self.nombre} | Correo: {self.correo}"
