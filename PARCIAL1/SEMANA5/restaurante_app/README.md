# Sistema básico de gestión de restaurante

Estudiante: Xavier Macías

## Descripción
Este proyecto implementa un sistema básico de gestión de restaurante utilizando Programación Orientada a Objetos en Python. El programa representa productos, clientes y un servicio principal que administra listas de objetos del sistema.

## Estructura del proyecto
- modelos/producto.py: define la clase Producto con atributos como nombre, precio, categoría, descripción, stock y disponibilidad.
- modelos/cliente.py: define la clase Cliente con atributos como nombre, teléfono, correo, edad y estado de membresía.
- servicios/restaurante.py: define la clase Restaurante para administrar listas de productos y clientes.
- main.py: crea objetos, los agrega al servicio principal y muestra la información en consola.

## Tipos de datos utilizados
- str: nombre, categoría, descripción, teléfono y correo.
- int: stock y edad.
- float: precio.
- bool: disponibilidad y membresía frecuente.
- list: listas de productos y clientes en la clase Restaurante.

## Reflexión
El uso de identificadores descriptivos, tipos de datos adecuados y listas permite organizar mejor el código, hacerlo más claro y facilitar su mantenimiento. En un proyecto modular, estas prácticas ayudan a comprender la lógica del sistema y a extenderlo en futuras actividades.
