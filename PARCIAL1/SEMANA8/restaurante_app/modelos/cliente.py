class Cliente:
    def __init__(self, identificacion: str, nombre: str, correo: str):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    def mostrar_informacion(self) -> str:
        return f"[{self.identificacion}] Cliente: {self.nombre} | Correo: {self.correo}"
