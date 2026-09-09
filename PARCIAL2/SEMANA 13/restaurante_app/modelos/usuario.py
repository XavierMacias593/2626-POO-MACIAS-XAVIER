class Usuario:
    """Representa un usuario del sistema."""

    def __init__(self, identificacion: str, nombre: str, correo: str, password: str = "1234") -> None:
        if not identificacion.strip() or not nombre.strip() or not correo.strip():
            raise ValueError("Identificación, nombre y correo son obligatorios.")

        self.identificacion = identificacion.strip()
        self.nombre = nombre.strip()
        self.correo = correo.strip()
        self.password = password

    def to_dict(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
            "password": self.password,
        }

    def mostrar_informacion(self) -> str:
        return f"[{self.identificacion}] {self.nombre} | Correo: {self.correo}"
