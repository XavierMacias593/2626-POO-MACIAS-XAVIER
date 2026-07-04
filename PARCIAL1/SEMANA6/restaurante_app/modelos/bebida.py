from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, precio, disponibilidad, volumen_ml):
        super().__init__(nombre, precio, disponibilidad)
        self.volumen_ml = volumen_ml  # Atributo específico de Bebida
        
    def mostrar_informacion(self):
        """Sobrescribe el método para mostrar información específica de Bebida (Polimorfismo)."""
        estado = "Disponible" if self.disponibilidad else "Agotado"
        print(f"Bebida: {self.nombre} | Volumen: {self.volumen_ml} ml | Precio: ${self.obtener_precio()} | Estado: {estado}")
