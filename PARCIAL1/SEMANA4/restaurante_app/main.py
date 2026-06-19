"""Punto de entrada: crea objetos, los agrega al servicio y muestra información."""

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():
    # Crear servicio principal
    restaurante = Restaurante("La Buena Mesa")

    # Crear algunos productos
    p1 = Producto("Lomo Saltado", 12.50, "Plato fuerte", "Carne salteada con papas y cebolla")
    p2 = Producto("Ceviche", 9.75, "Entrada", "Pescado fresco marinado en limón")
    p3 = Producto("Inca Kola 500ml", 2.00, "Bebida", "Refresco tradicional")

    # Agregar productos al restaurante
    restaurante.agregar_producto(p1)
    restaurante.agregar_producto(p2)
    restaurante.agregar_producto(p3)

    # Crear y registrar clientes
    c1 = Cliente("María Pérez", telefono="+591-71234567")
    c2 = Cliente("Carlos López", email="carlos.lopez@example.com")

    restaurante.registrar_cliente(c1)
    restaurante.registrar_cliente(c2)

    # Mostrar resumen inicial
    restaurante.mostrar_resumen()

    # Aplicar un descuento a un producto y mostrar el cambio
    print('\nAplicando descuento del 10% a Ceviche...')
    prod = restaurante.buscar_producto("ceviche")
    if prod:
        prod.aplicar_descuento(10)
    restaurante.listar_productos()


if __name__ == "__main__":
    main()
