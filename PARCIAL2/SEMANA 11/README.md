# Semana 11 - Sistema de restaurante

**Estudiante:** Xavier Macías

## Descripción

Esta versión evoluciona `restaurante_app` de la Semana 10. Además de administrar productos y usuarios, registra ventas que relacionan un usuario con un producto, controla el stock y conserva toda la información en archivos JSON.

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
└── main.py
```

## Responsabilidades

- `Producto`: valida datos, conserva precio y stock, descuenta unidades mediante `vender()` y se convierte a diccionario JSON.
- `Usuario`: valida sus datos y ofrece `to_dict()` para persistencia.
- `Venta`: conserva `usuario_id`, `producto_codigo` y `cantidad`.
- `Restaurante`: administra colecciones, búsquedas, operaciones de venta y consulta filtrada de ventas.
- `ArchivoServicio`: carga y guarda productos, usuarios y ventas con `json.load()` y `json.dump()`.
- `main.py`: solicita datos con `input()` y coordina las operaciones sin modificar colecciones internas.

## Funcionamiento de ventas y stock

`vender_producto()` comprueba que existan usuario y producto, que la cantidad sea un entero positivo y que haya stock suficiente. Solo después crea una `Venta`, la agrega a la colección y descuenta el stock. El stock nunca puede ser negativo.

La consulta de ventas recorre la colección y devuelve únicamente las ventas cuyo `usuario_id` coincide con la identificación indicada.

## Persistencia y excepciones

Al iniciar se recuperan las tres colecciones desde `datos/productos.json`, `usuarios.json` y `ventas.json`. Después de cambios en productos o usuarios se guarda su archivo; una venta guarda `ventas.json` y el stock actualizado en `productos.json`.

Se controlan `FileNotFoundError` iniciando con una colección vacía, `json.JSONDecodeError` para archivos inválidos, `PermissionError` para problemas de acceso, `KeyError` para claves faltantes y `TypeError`/`ValueError` para registros inválidos.

## Ejecución

Desde `restaurante_app`:

```bash
python main.py
```

## Pruebas realizadas

- Registro y recuperación de productos, usuarios y ventas.
- Venta válida con disminución de stock.
- Rechazo de cantidad cero, cantidades no enteras y stock insuficiente sin alterar los datos.
- Consulta de ventas filtrada por identificación de usuario.
- Inicio con archivos JSON inexistentes o inválidos.
