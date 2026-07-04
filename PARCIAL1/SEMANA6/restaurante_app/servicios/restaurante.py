class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []  # Lista para almacenar los productos
        
    def agregar_producto(self, producto):
        """Agrega un producto a la lista del restaurante."""
        self.productos.append(producto)
        print(f"Se ha agregado '{producto.nombre}' al restaurante {self.nombre}.")
        
    def mostrar_menu(self):
        """Recorre la lista de productos y ejecuta mostrar_informacion() demostrando polimorfismo."""
        print(f"\n--- Menú de {self.nombre} ---")
        if not self.productos:
            print("El menú está vacío.")
        for producto in self.productos:
            producto.mostrar_informacion()  # Polimorfismo en acción
        print("-----------------------------\n")
