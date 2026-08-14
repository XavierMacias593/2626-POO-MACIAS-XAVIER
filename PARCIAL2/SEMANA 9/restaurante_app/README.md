# Semana 9 - Sistema de restaurante

Estudiante: Xavier Macías

## Descripción
Este proyecto continúa el desarrollo del sistema de restaurante utilizando programación orientada a objetos y estructuras de datos de Python. La diferencia principal con versiones anteriores es que ahora se administra la información en colecciones organizadas, manteniendo una separación clara entre los modelos, el servicio y la interacción con el usuario.

## Estructura del proyecto

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
├── README.md
```

## Responsabilidad de cada componente

- modelos/producto.py: contiene la clase Producto con información de código, nombre, categoría y precio.
- modelos/usuario.py: contiene la clase Usuario con información general como identificación, nombre y correo.
- servicios/restaurante.py: administra las colecciones, validaciones y operaciones del sistema.
- main.py: controla el menú interactivo y coordina la entrada de datos con el servicio.

## Uso de estructuras de datos

### Listas (`list`)
Se utilizan listas para manejar colecciones dinámicas de productos y usuarios. En la clase Restaurante se mantienen las listas `self.productos` y `self.usuarios` para registrar, buscar, actualizar, eliminar y listar información en tiempo real.

### Tuplas (`tuple`)
Se usa una tupla para guardar las opciones del menú principal, porque deben mantenerse estables durante la ejecución del sistema y no necesitan modificarse dinámicamente. Esta información está definida en `self.opciones_menu` dentro de la clase `Restaurante`.

### Diccionarios (`dict`)
Se usa un diccionario para asociar cada opción del menú con la acción correspondiente. Esto facilita la organización del código y permite relacionar claves como `"1"` y valores como `"registrar_producto"` de manera clara y funcional.

### Conjuntos (`set`)
Se usa un conjunto para mostrar categorías sin duplicados. La operación `mostrar_categorias()` recorre todos los productos y agrega las categorías en un `set`, evitando repeticiones y presentando solo valores únicos.

## Funcionalidades principales

- Registrar productos.
- Buscar productos por código.
- Actualizar datos de un producto.
- Eliminar productos.
- Listar productos.
- Registrar usuarios.
- Listar usuarios.
- Mostrar categorías de productos sin duplicados.

## Reglas del sistema

- No se permiten códigos de productos repetidos.
- No se permiten identificaciones de usuarios repetidas.
- La lógica de administración de datos se mantiene dentro del servicio `Restaurante`.
- El archivo `main.py` solo solicita información y llama a los métodos del servicio.

## Ejecución

Para ejecutar el proyecto se debe abrir la carpeta del proyecto y correr el archivo principal:

```bash
python main.py
```

## Reflexión
La selección adecuada de una estructura de datos es fundamental porque cada una tiene una finalidad distinta. Las listas permiten almacenar colecciones dinámicas, las tuplas representan información estable, los diccionarios relacionan claves con valores y los conjuntos evitan duplicados. Elegir la estructura correcta hace que el programa sea más ordenado, eficiente y fácil de mantener.
