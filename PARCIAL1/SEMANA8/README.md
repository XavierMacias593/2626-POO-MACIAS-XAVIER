# Sistema de Restaurante

## Descripción del Sistema
El sistema `restaurante_app` es una aplicación de consola desarrollada en Python para gestionar productos, bebidas y clientes de un restaurante. Se basa en el paradigma de la Programación Orientada a Objetos y aplica los principios SOLID (Responsabilidad Única, Abierto/Cerrado y Sustitución de Liskov).

## Estructura del Proyecto
```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```

## Responsabilidad de cada clase (SRP - Responsabilidad Única)
- **Producto (`modelos/producto.py`)**: Representa la información base de los productos del restaurante. Define atributos comunes como el código, nombre, categoría y precio, y provee el método `mostrar_informacion()`.
- **Bebida (`modelos/bebida.py`)**: Especializa a la clase `Producto`, incorporando propiedades específicas como el tamaño y tipo de envase.
- **Cliente (`modelos/cliente.py`)**: Gestiona la información de los clientes (identificación, nombre, correo). Su única responsabilidad es mantener estos datos.
- **Restaurante (`servicios/restaurante.py`)**: Clase de servicio que administra las colecciones (listas) de productos y clientes. Contiene la lógica de negocio para registrar, validar (evitar duplicados) y listar las entidades.
- **`main.py`**: Interfaz de usuario por consola. Muestra el menú, recolecta datos mediante `input()` y coordina las llamadas a los métodos del servicio.

## Principios OCP y LSP aplicados
- **Abierto/Cerrado (OCP)**: El sistema está abierto a su extensión y cerrado a su modificación. Al incorporar la clase `Bebida`, el servicio `Restaurante` no necesitó modificar su método de registro o listado, ya que simplemente acepta cualquier objeto que sea un `Producto`.
- **Sustitución de Liskov (LSP)**: Una instancia de `Bebida` se puede usar donde se espera una instancia de `Producto` sin causar errores. Ambas clases responden al método `mostrar_informacion()`. La clase `Restaurante` administra la lista de productos y ejecuta `producto.mostrar_informacion()` con confianza, aplicando el polimorfismo, sin necesidad de preguntar si el objeto es una bebida.

## Instrucciones de Ejecución
1. Abra la consola o terminal.
2. Navegue hasta el directorio `restaurante_app`.
3. Ejecute el comando: `python main.py`
4. Interactúe con el menú ingresando los números de las opciones.

## Reflexión sobre la importancia de diseñar proyectos mantenibles
La aplicación de los principios SOLID en el diseño de un proyecto, combinada con una arquitectura modular y orientada a responsabilidades, es fundamental para crear sistemas fáciles de mantener, probar y extender. Si cada clase tiene un único propósito, los cambios en una funcionalidad afectan una parte mínima y controlada del sistema. Esto ahorra tiempo y esfuerzo a largo plazo, ya que reduce los errores cuando los requerimientos evolucionan.
