from modelos.producto import Producto

class Platillo(Producto):
    def __init__(self, nombre, precio, disponibilidad, calorias):
        super().__init__(nombre, precio, disponibilidad)
        self.calorias = calorias  # Atributo específico de Platillo
        
    def mostrar_informacion(self):
        """Sobrescribe el método para mostrar información específica de Platillo (Polimorfismo)."""
        estado = "Disponible" if self.disponibilidad else "Agotado"
        print(f"Platillo: {self.nombre} | Calorías: {self.calorias} kcal | Precio: ${self.obtener_precio()} | Estado: {estado}")
