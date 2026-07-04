class Producto:
    def __init__(self, nombre, precio, disponibilidad=True):
        self.nombre = nombre
        self.__precio = precio  # Atributo encapsulado
        self.disponibilidad = disponibilidad
    
    def obtener_precio(self):
        """Devuelve el precio actual del producto."""
        return self.__precio
    
    def cambiar_precio(self, nuevo_precio):
        """Modifica el precio validando que sea mayor a 0."""
        if nuevo_precio > 0:
            precio_anterior = self.__precio
            self.__precio = nuevo_precio
            print(f"Exito: El precio de '{self.nombre}' ha cambiado de ${precio_anterior} a ${self.__precio}.")
        else:
            print(f"Error al cambiar precio de '{self.nombre}': El precio no puede ser negativo ni igual a cero (Intentó: ${nuevo_precio}).")
    
    def mostrar_informacion(self):
        """Muestra la información general del producto."""
        estado = "Disponible" if self.disponibilidad else "Agotado"
        print(f"Producto: {self.nombre} | Precio: ${self.__precio} | Estado: {estado}")
