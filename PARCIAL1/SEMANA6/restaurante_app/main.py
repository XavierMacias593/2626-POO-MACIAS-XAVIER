from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def main():
    # Instanciar el servicio
    mi_restaurante = Restaurante("El Buen Sabor")
    
    # Crear objetos (2 Platillos, 2 Bebidas)
    platillo1 = Platillo("Enchiladas Suizas", 120.50, True, 600)
    platillo2 = Platillo("Tacos de Pastor", 85.00, True, 800)
    
    bebida1 = Bebida("Refresco de Cola", 25.00, True, 600)
    bebida2 = Bebida("Agua de Horchata", 20.00, False, 1000)
    
    # Agregar productos al restaurante
    mi_restaurante.agregar_producto(platillo1)
    mi_restaurante.agregar_producto(platillo2)
    mi_restaurante.agregar_producto(bebida1)
    mi_restaurante.agregar_producto(bebida2)
    
    # Mostrar el menú (evidenciando polimorfismo)
    mi_restaurante.mostrar_menu()
    
    # Probar encapsulación (cambiar precio)
    print("\n--- Modificando Precios (Prueba de Encapsulación) ---")
    platillo1.cambiar_precio(130.00)
    bebida1.cambiar_precio(-10.00)  # Esto debe mostrar un error debido a la validación
    print("-----------------------------------------------------")
    
    # Mostrar el menú actualizado
    mi_restaurante.mostrar_menu()

if __name__ == "__main__":
    main()
