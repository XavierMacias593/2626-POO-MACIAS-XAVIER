# Semana 13 - Restaurante App con Tkinter

Esta semana se inicia la base gráfica del proyecto `restaurante_app` usando `Tkinter`, manteniendo la misma organización de capas que el proyecto docente de la semana 13.

## Objetivo

Crear una estructura base para una interfaz gráfica que permita:

- iniciar sesión con usuario y contraseña simulados,
- mostrar una vista principal del restaurante,
- consultar productos registrados desde `productos.json`,
- consultar usuarios registrados desde `usuarios.json`,
- mantener la lógica del negocio separada de la interfaz.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```

## Flujo de la aplicación

1. Se inicia la aplicación desde `main.py`.
2. Se muestra la pantalla de acceso `LoginView`.
3. El usuario ingresa sus credenciales.
4. `RestauranteServicio` valida el acceso.
5. Si la validación es correcta, se muestra `MainView`.
6. La vista principal muestra productos y usuarios.
7. La opción de ventas queda marcada como pendiente para etapas futuras.
8. Se puede cerrar sesión y volver al login dentro de la misma ventana.

## Ejecución

```bash
cd restaurante_app
python main.py
```

## Credenciales de prueba

Se incluyen usuarios de ejemplo en el archivo JSON para validar la simulación de acceso:

- Usuario: `admin`
- Contraseña: `1234`

- Usuario: `juan`
- Contraseña: `1234`

## Notas

- La lectura de datos se realiza desde `ArchivoServicio`.
- La lógica de acceso y consulta de información se concentra en `RestauranteServicio`.
- Las vistas no leen JSON directamente.
- Esta es una primera base gráfica y no incluye todavía todas las funciones del restaurante en consola.
