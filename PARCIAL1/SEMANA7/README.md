# Sistema de restaurante con Programación Orientada a Objetos

Estudiante: Xavier Macias

## Descripción del sistema
Este proyecto implementa un sistema básico de gestión de un restaurante utilizando Programación Orientada a Objetos en Python. Permite registrar, listar y buscar productos y clientes desde un menú interactivo ejecutado en consola.

## Estructura del proyecto
- modelos/producto.py: contiene la clase Producto implementada con constructor tradicional __init__, propiedades y setters.
- modelos/cliente.py: contiene la clase Cliente implementada con el decorador @dataclass.
- servicios/restaurante.py: contiene la clase Restaurante encargada de administrar listas de productos y clientes.
- main.py: punto de entrada del programa, donde se muestra el menú interactivo.

## Conceptos aplicados
- Constructor en la clase Producto mediante __init__.
- Decoradores @property y @setter para controlar el acceso y validación de atributos.
- Decorador @dataclass en la clase Cliente.
- Creación dinámica de objetos a partir de datos ingresados por el usuario.

## Menú interactivo
El programa presenta un menú con opciones para:
1. Registrar producto
2. Listar productos
3. Buscar producto
4. Registrar cliente
5. Listar clientes
6. Buscar cliente
7. Salir

## Reflexión
Crear objetos a partir de datos ingresados por el usuario permite que el sistema sea flexible, realista y fácil de extender, además de demostrar de manera práctica cómo la POO organiza la lógica de una aplicación.
