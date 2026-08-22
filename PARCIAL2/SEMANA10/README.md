# Semana 10 - Sistema de restaurante

**Estudiante:** Xavier Macías

## Descripción

Evolución del sistema de restaurante de la Semana 9. El programa administra productos y usuarios mediante clases y ahora conserva únicamente los productos en `restaurante_app/datos/productos.json`.

## Estructura

```text
restaurante_app/
├── datos/
│   └── productos.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
```

## Responsabilidades

- `Producto`: valida sus datos y ofrece `to_dict()` para serializarse.
- `Usuario`: representa usuarios, que permanecen en memoria.
- `Restaurante`: administra registros, búsquedas, actualizaciones, eliminaciones y listados.
- `ArchivoServicio`: concentra la lectura y escritura de productos usando JSON.
- `main.py`: carga al iniciar, coordina el menú y guarda después de cada cambio exitoso.

## Persistencia JSON

Al iniciar, `ArchivoServicio.cargar_productos()` abre el archivo con `with open(..., encoding="utf-8")`, ejecuta `json.load()` y valida cada registro. Los registros válidos se reconstruyen como objetos `Producto` antes de entregarlos a `Restaurante`.

Después de registrar, actualizar o eliminar correctamente, `main.py` solicita a `ArchivoServicio.guardar_productos()` la conversión mediante `to_dict()` y la escritura con `json.dump()`. El archivo contiene una lista legible de diccionarios.

Se controlan `FileNotFoundError` para el primer inicio, `JSONDecodeError` para archivos dañados, `PermissionError` para problemas de acceso, `KeyError` para claves faltantes y `ValueError`/`TypeError` para datos inválidos. Un registro defectuoso se omite sin detener el resto de la aplicación.

## Ejecución

Desde la carpeta `restaurante_app`:

```bash
python main.py
```

## Comprobación realizada

Se registró un producto y se verificó que apareció en `datos/productos.json`. Después se ejecutó nuevamente `main.py` y el producto se mostró mediante listar. También se actualizaron y eliminaron productos; al reiniciar, el archivo conservó cada cambio.
