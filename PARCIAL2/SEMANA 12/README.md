# Semana 12 - restaurante_app mejorado con colecciones

Esta carpeta contiene la evolución de la aplicación de restaurante desarrollada durante la Semana 11, aplicando mejoras de rendimiento mediante estructuras auxiliares con `dict` para búsquedas rápidas y validaciones frecuentes.

## Mejoras realizadas

- Se conservaron las listas principales de productos, usuarios y ventas para persistir y recorrer la información.
- Se agregaron índices en memoria para buscar productos por código y usuarios por identificación.
- Se optimizó la consulta de ventas por usuario usando un diccionario que agrupa ventas por clave de usuario.
- Los índices se reconstruyen al iniciar la aplicación desde los JSON cargados.
- La lógica de negocio sigue siendo responsabilidad del servicio `Restaurante`, sin trasladar lógica a `main.py`.

## Estructura

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
├── README.md
└── __pycache__/
```

## Ejecución

```bash
cd restaurante_app
python main.py
```

## Pruebas principales realizadas

- Registro y consulta de productos.
- Registro y búsqueda de usuarios.
- Venta con validación de stock.
- Consulta de ventas por usuario.
- Recuperación de datos desde JSON y reconstrucción de índices tras reiniciar la aplicación.

## Observaciones

La mejora aplicada se centra en optimizar búsquedas repetitivas sin reemplazar las colecciones principales por diccionarios completos, manteniendo así la coherencia del modelo y la persistencia del sistema.
