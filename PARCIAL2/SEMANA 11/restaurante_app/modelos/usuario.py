class Usuario:
    """Representa a una persona registrada en el restaurante."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        if not identificacion.strip() or not nombre.strip() or not correo.strip():
            raise ValueError("Los datos del usuario son obligatorios.")
        self.identificacion = identificacion.strip()
        self.nombre = nombre.strip()
        self.correo = correo.strip()

    def to_dict(self) -> dict[str, str]:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
        }

    def mostrar_informacion(self) -> str:
        return f"[{self.identificacion}] {self.nombre} | Correo: {self.correo}"
