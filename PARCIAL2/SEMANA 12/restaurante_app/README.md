# restaurante_app - Semana 12

Aplicación de consola para administrar productos, usuarios, ventas y control de stock con mejoras de eficiencia en búsquedas y consultas mediante colecciones auxiliares.

## Qué se mejoró

La aplicación conserva la estructura funcional de la Semana 11, pero incorpora índices en memoria para optimizar las operaciones más frecuentes:

- `dict` para buscar productos por código.
- `dict` para buscar usuarios por identificación.
- `dict` de ventas agrupadas por usuario para consultar ventas sin recorrer toda la lista.

## Colecciones utilizadas

- Listas: se mantienen para almacenar, listar y persistir objetos en JSON.
- Diccionarios: se usan como índices rápidos para claves conocidas.
- Set: no se utilizó porque no fue necesario para una validación de pertenencia o unicidad crítica dentro de este sistema.

## Ejecución

```bash
python main.py
```

## Contenido principal

- `modelos/`: clases del dominio.
- `servicios/archivo_servicio.py`: carga y guarda datos en JSON.
- `servicios/restaurante.py`: lógica de negocio y optimización con índices.
- `main.py`: menú de consola y flujo principal.

## Pruebas realizadas

- Registro de productos y usuarios.
- Búsqueda por código e identificación.
- Venta validando stock y actualizando cantidades.
- Consulta de ventas por usuario.
- Verificación de persistencia y reconstrucción de índices luego de reiniciar la app.
