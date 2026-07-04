# Restaurante App

**Estudiante:** [Tu Nombre Completo]

## Descripción del Sistema
Este es un sistema básico de administración de productos para un restaurante, desarrollado en Python aplicando los principios de la Programación Orientada a Objetos (POO).

## Estructura del Proyecto
El proyecto está dividido de forma modular:
- `modelos/`: Contiene las clases de las entidades (`Producto`, `Platillo`, `Bebida`).
- `servicios/`: Contiene la lógica de negocio, como la clase `Restaurante` que administra los productos.
- `main.py`: Archivo principal que ejecuta y prueba la aplicación.

## Principios de POO Aplicados
1. **Herencia:** Las clases `Platillo` y `Bebida` heredan atributos y métodos de la clase padre `Producto`.
2. **Encapsulación:** El atributo `__precio` en la clase `Producto` está protegido para evitar modificaciones directas no válidas. Se controla a través de `obtener_precio()` y `cambiar_precio()`.
3. **Polimorfismo:** El método `mostrar_informacion()` está definido en `Producto` y sobrescrito en `Platillo` y `Bebida`. Al iterar sobre la lista de productos en el menú, Python ejecuta la versión correcta del método dependiendo del tipo de objeto.

## Reflexión
Aplicar los principios de POO en proyectos modulares permite que el código sea mucho más reutilizable, escalable y fácil de mantener. Al separar las responsabilidades en diferentes archivos, es más sencillo encontrar y corregir errores o agregar nuevas funcionalidades en el futuro.
