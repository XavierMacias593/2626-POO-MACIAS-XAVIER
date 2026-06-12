class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self) -> None:
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad} años")

    def hacer_sonido(self) -> None:
        sonidos = {
            "Perro": "Guau guau!",
            "Gato": "Miau miau!",
            "Pájaro": "Pío pío!",
            "Conejo": "Sniff sniff!",
        }
        sonido = sonidos.get(self.especie, "... (silencio) ...")
        print(f"{self.nombre} hace: {sonido}")
