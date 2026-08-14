"""Punto de entrada del sistema de gestión del restaurante."""

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():
    # Crear el servicio principal del restaurante.
    restaurante = Restaurante("La Buena Mesa")

    # Crear dos productos de ejemplo con datos de tipo str, float, int y bool.
    producto_uno = Producto("Lomo Saltado", 15.50, "Plato fuerte", "Carne salteada con arroz y papas", 8, True)
    producto_dos = Producto("Jugo de Maracuyá", 3.20, "Bebida", "Bebida natural fresca", 12, True)
    producto_tres = Producto("Ensalada César", 8.90, "Entrada", "Lechuga, pollo y aderezo", 5, True)

    # Crear dos clientes de ejemplo con atributos de tipo str, int y bool.
    cliente_uno = Cliente("María Pérez", "+591 71234567", "maria@example.com", 28, True)
    cliente_dos = Cliente("Carlos López", "+591 70567890", "carlos@example.com", 35, False)

    # Agregar los objetos a las listas manejadas por el servicio.
    restaurante.agregar_producto(producto_uno)
    restaurante.agregar_producto(producto_dos)
    restaurante.agregar_producto(producto_tres)

    restaurante.registrar_cliente(cliente_uno)
    restaurante.registrar_cliente(cliente_dos)

    # Mostrar la información registrada en la consola.
    restaurante.mostrar_resumen()

    # Aplicar una modificación adicional para demostrar el uso de los métodos.
    print("\nActualizando stock y estado de membresía...")
    producto_dos.actualizar_stock(-3)
    cliente_uno.cambiar_estado_miembro(True)
    print(f"Producto actualizado: {producto_dos}")
    print(f"Cliente actualizado: {cliente_uno}")


if __name__ == "__main__":
    main()
