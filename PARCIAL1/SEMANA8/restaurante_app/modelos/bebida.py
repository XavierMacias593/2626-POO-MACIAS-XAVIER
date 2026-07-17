from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tamano: str, tipo_envase: str):
        super().__init__(codigo, nombre, categoria, precio)
        self.tamano = tamano
        self.tipo_envase = tipo_envase

    def mostrar_informacion(self) -> str:
        return f"[{self.codigo}] Bebida: {self.nombre} | Categoría: {self.categoria} | Tamaño: {self.tamano} | Envase: {self.tipo_envase} | Precio: ${self.precio:.2f}"
