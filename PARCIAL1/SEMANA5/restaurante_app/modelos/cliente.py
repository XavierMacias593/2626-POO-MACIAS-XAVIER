# Clase que representa a un cliente registrado en el restaurante.
class Cliente:
    def __init__(self, nombre: str, telefono: str = "", email: str = "", edad: int = 0, miembro_frecuente: bool = False):
        """Inicializa un cliente con datos personales y estado de membresía."""
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.edad = int(edad)
        self.miembro_frecuente = bool(miembro_frecuente)

    def actualizar_contacto(self, telefono: str = "", email: str = "") -> None:
        """Actualiza los datos de contacto del cliente."""
        if telefono:
            self.telefono = telefono
        if email:
            self.email = email

    def cambiar_estado_miembro(self, miembro_frecuente: bool) -> None:
        """Cambia el estado de membresía del cliente."""
        self.miembro_frecuente = bool(miembro_frecuente)

    def mostrar_resumen(self) -> str:
        """Devuelve un resumen del cliente."""
        estado = "Sí" if self.miembro_frecuente else "No"
        return f"{self.nombre} | Edad: {self.edad} | Miembro frecuente: {estado}"

    def __str__(self) -> str:
        partes = [f"Nombre: {self.nombre}", f"Edad: {self.edad}"]
        if self.telefono:
            partes.append(f"Tel: {self.telefono}")
        if self.email:
            partes.append(f"Email: {self.email}")
        estado = "Miembro frecuente" if self.miembro_frecuente else "Visitante"
        partes.append(estado)
        return " | ".join(partes)
