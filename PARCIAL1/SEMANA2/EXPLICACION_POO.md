# 📚 Explicación Detallada: Programación Orientada a Objetos (POO)

## Índice
1. [¿Qué es POO?](#qué-es-poo)
2. [Concepto de Clase y Objeto](#concepto-de-clase-y-objeto)
3. [Estructura del Código](#estructura-del-código)
4. [Atributos](#atributos)
5. [Métodos](#métodos)
6. [El Constructor (`__init__`)](#el-constructor-init)
7. [Explicación Línea por Línea](#explicación-línea-por-línea)
8. [Cómo se Usa el Programa](#cómo-se-usa-el-programa)

---

## ¿Qué es POO?

### Definición Simple
**Programación Orientada a Objetos (POO)** es una forma de escribir código que organiza los datos y las acciones de manera más natural, como los objetos del mundo real.

### Analogía del Mundo Real
Imagina que quieres guardar información sobre un **libro**:

**Sin POO (Programación Procedural):**
```python
# Tendrías variables sueltas por todos lados
titulo_libro1 = "El Quijote"
autor_libro1 = "Miguel de Cervantes"
paginas_libro1 = 863

titulo_libro2 = "1984"
autor_libro2 = "George Orwell"
paginas_libro2 = 328
```

**Con POO:**
```python
# Todo relacionado al libro está junto en una clase
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
```

### Ventajas de POO
- ✅ **Organización**: Todo lo del libro está junto
- ✅ **Reutilización**: Puedes crear muchos libros sin repetir código
- ✅ **Claridad**: El código es más fácil de entender
- ✅ **Mantenimiento**: Cambios en un lugar = cambios en todo

---

## Concepto de Clase y Objeto

### ¿Qué es una Clase?
Una **clase** es como un **molde o plantilla** que define qué características y comportamientos tienen las cosas.

```
ANALOGÍA: Si quieres hacer muchas galletas del mismo tipo, 
necesitas un molde. La clase es el molde.
```

### ¿Qué es un Objeto?
Un **objeto** es una **instancia específica** creada a partir de la clase.

```
ANALOGÍA: Las galletas que sacas del molde son los objetos. 
Cada galleta es diferente (tiene diferentes sabores, decoraciones), 
pero todas fueron hechas con el mismo molde.
```

### Ejemplo en el Código:

```python
# Esto es la CLASE (el molde)
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

# Esto es crear OBJETOS (galletas del molde)
libro1 = Libro("El Quijote", "Miguel de Cervantes", 863)
libro2 = Libro("1984", "George Orwell", 328)
libro3 = Libro("Cien años de soledad", "Gabriel García Márquez", 417)
```

**Resultado:**
- `libro1`, `libro2` y `libro3` son **tres objetos diferentes**
- Todos creados de la clase `Libro`
- Cada uno tiene sus propios valores

---

## Estructura del Código

### Partes Principales de una Clase

```python
class NombreDeLaClase:
    # 1. ATRIBUTOS DE CLASE (opcional)
    atributo_compartido = 0
    
    # 2. CONSTRUCTOR (especial)
    def __init__(self, parametros):
        # Aquí inicializamos los atributos
        self.atributo1 = valor1
        self.atributo2 = valor2
    
    # 3. MÉTODOS (funciones dentro de la clase)
    def método1(self):
        # Hacer algo
        pass
    
    def método2(self, parámetro):
        # Hacer algo con el parámetro
        pass
```

---

## Atributos

Los atributos son las **características o propiedades** que tiene un objeto.

### Tipos de Atributos

#### 1. **Atributos de Instancia**
Cada objeto tiene sus propios valores, independientes de otros objetos.

```python
def __init__(self, titulo, autor, paginas, año_publicacion, disponible=True):
    # Estos son atributos de instancia
    self.titulo = titulo
    self.autor = autor
    self.paginas = paginas
    self.año_publicacion = año_publicacion
    self.disponible = disponible
    self.páginas_leídas = 0
```

**Explicación:**
- `self` = la palabra clave que se refiere al objeto actual
- `self.titulo` = el objeto ESTE LIBRO tendrá un atributo llamado `titulo`
- Cada libro tiene su propio título diferente

**Ejemplo:**
```python
libro1 = Libro("El Quijote", "Cervantes", 863, 1605)
libro2 = Libro("1984", "Orwell", 328, 1949)

print(libro1.titulo)  # Imprime: "El Quijote"
print(libro2.titulo)  # Imprime: "1984"
```

#### 2. **Atributos de Clase**
Compartidos por TODAS las instancias (todos los objetos).

```python
class Libro:
    cantidad_libros_creados = 0  # Atributo de clase
    
    def __init__(self, titulo, autor, paginas, año_publicacion, disponible=True):
        self.titulo = titulo
        # ...
        Libro.cantidad_libros_creados += 1  # Incrementar el contador compartido
```

**Explicación:**
- Este contador es el MISMO para todos los libros
- Cuando creas un nuevo libro, se suma 1
- Se accede con `NombreDeLaClase.atributo`

**Ejemplo:**
```python
libro1 = Libro("El Quijote", "Cervantes", 863, 1605)
libro2 = Libro("1984", "Orwell", 328, 1949)
libro3 = Libro("Cien años", "Márquez", 417, 1967)

print(Libro.cantidad_libros_creados)  # Imprime: 3
```

---

## Métodos

Los métodos son las **acciones o comportamientos** que pueden hacer los objetos.

### Tipos de Métodos

#### 1. **Métodos de Instancia** (Los más comunes)
Reciben `self` como primer parámetro y actúan sobre un objeto específico.

```python
def leer_páginas(self, cantidad_páginas):
    """
    Simula la lectura de un número de páginas
    """
    if not self.disponible:
        print("⚠️  El libro no está disponible para lectura.")
        return
    
    if cantidad_páginas <= 0:
        print("⚠️  Debe especificar un número válido de páginas.")
        return
    
    if self.páginas_leídas + cantidad_páginas > self.paginas:
        páginas_restantes = self.paginas - self.páginas_leídas
        print(f"⚠️  Solo hay {páginas_restantes} páginas restantes para leer.")
        self.páginas_leídas = self.paginas
    else:
        self.páginas_leídas += cantidad_páginas
        print(f"✓ Se han leído {cantidad_páginas} páginas exitosamente.")
```

**Ejemplo de uso:**
```python
libro1 = Libro("El Quijote", "Cervantes", 863, 1605)
libro1.leer_páginas(100)  # El libro LEE 100 páginas
```

#### 2. **Métodos Estáticos** (@staticmethod)
No reciben `self` ni `cls`, son funciones dentro de la clase que no dependen de ningún objeto.

```python
@staticmethod
def comparar_libros(libro1, libro2):
    """
    Método estático que compara dos libros por número de páginas
    """
    if libro1.paginas > libro2.paginas:
        return f"'{libro1.titulo}' tiene más páginas ({libro1.paginas})"
    elif libro1.paginas < libro2.paginas:
        return f"'{libro2.titulo}' tiene más páginas ({libro2.paginas})"
    else:
        return f"Ambos libros tienen la misma cantidad de páginas ({libro1.paginas})"
```

**Explicación:**
- No necesita un objeto específico
- Se accede con `NombreDeLaClase.método()`

**Ejemplo:**
```python
libro1 = Libro("El Quijote", "Cervantes", 863, 1605)
libro2 = Libro("1984", "Orwell", 328, 1949)

# No necesitamos un objeto específico
resultado = Libro.comparar_libros(libro1, libro2)
print(resultado)  # "El Quijote" tiene más páginas (863)
```

#### 3. **Métodos de Clase** (@classmethod)
Reciben `cls` (la clase) en lugar de `self`, actúan sobre la clase completa.

```python
@classmethod
def obtener_cantidad_libros(cls):
    """
    Método de clase que retorna la cantidad total de libros creados
    """
    return cls.cantidad_libros_creados
```

**Ejemplo:**
```python
libro1 = Libro("El Quijote", "Cervantes", 863, 1605)
libro2 = Libro("1984", "Orwell", 328, 1949)

# Obtener el total de libros
total = Libro.obtener_cantidad_libros()
print(f"Se han creado {total} libros")  # Se han creado 2 libros
```

#### 4. **Métodos Especiales** (Dunder methods)
Tienen nombres especiales con dobles guiones: `__nombre__`

```python
def __str__(self):
    """
    Se llama cuando usas print() o str() en el objeto
    """
    return f"'{self.titulo}' por {self.autor}"

def __repr__(self):
    """
    Se llama cuando quieres ver la representación técnica del objeto
    """
    return f"Libro(titulo='{self.titulo}', autor='{self.autor}', paginas={self.paginas})"
```

**Ejemplo:**
```python
libro1 = Libro("El Quijote", "Cervantes", 863, 1605)

print(libro1)        # Usa __str__: 'El Quijote' por Cervantes
print(repr(libro1))  # Usa __repr__: Libro(titulo='El Quijote', autor='Cervantes', paginas=863)
```

---

## El Constructor (`__init__`)

El constructor es un método especial que se ejecuta **automáticamente** cuando creas un nuevo objeto.

### ¿Qué hace?
Inicializa (prepara) el objeto con sus valores iniciales.

### Estructura

```python
def __init__(self, titulo, autor, paginas, año_publicacion, disponible=True):
    """
    Constructor - Inicializa los atributos del libro
    
    Parámetros:
        titulo (str): El título del libro
        autor (str): El nombre del autor
        paginas (int): Número de páginas del libro
        año_publicacion (int): Año de publicación
        disponible (bool): Si el libro está disponible (por defecto True)
    """
    # Atributos de instancia
    self.titulo = titulo
    self.autor = autor
    self.paginas = paginas
    self.año_publicacion = año_publicacion
    self.disponible = disponible
    self.páginas_leídas = 0
    
    # Incrementar contador de libros
    Libro.cantidad_libros_creados += 1
```

### Parámetros Explicados

| Parámetro | Tipo | Ejemplo | Explicación |
|-----------|------|---------|-------------|
| `self` | (automático) | - | Se refiere al objeto actual |
| `titulo` | `str` | "El Quijote" | El nombre del libro |
| `autor` | `str` | "Cervantes" | Quién escribió el libro |
| `paginas` | `int` | 863 | Número de páginas |
| `año_publicacion` | `int` | 1605 | Cuándo se publicó |
| `disponible` | `bool` | True | ¿Se puede leer? (por defecto True) |

### Parámetros Opcionales
Algunos parámetros tienen un valor por defecto:

```python
def __init__(self, ..., disponible=True):
    # Si no especificas 'disponible', será True
```

**Ejemplo:**
```python
# Sin especificar disponible (usará True)
libro1 = Libro("El Quijote", "Cervantes", 863, 1605)
print(libro1.disponible)  # True

# Especificando disponible como False
libro2 = Libro("1984", "Orwell", 328, 1949, False)
print(libro2.disponible)  # False
```

---

## Explicación Línea por Línea

### Parte 1: Definición de la Clase y Documentación

```python
class Libro:
    """
    Clase que representa un libro con sus atributos y métodos.
    Un libro es un ejemplo de objeto del mundo real que tiene propiedades
    y comportamientos que podemos modelar en código.
    """
```

**Explicación:**
- `class Libro:` → Define una nueva clase llamada "Libro"
- El bloque de comentarios (entre `"""`) es la documentación (docstring)
- Cuando alguien llame `help(Libro)` en Python, verá esto

### Parte 2: Atributo de Clase

```python
# Atributo de clase (compartido por todas las instancias)
cantidad_libros_creados = 0
```

**Explicación:**
- Esta variable es compartida por TODOS los objetos Libro
- Se usa para contar cuántos libros se han creado

### Parte 3: El Constructor

```python
def __init__(self, titulo, autor, paginas, año_publicacion, disponible=True):
    """
    Constructor - Inicializa los atributos del libro
    ...
    """
    # Atributos de instancia
    self.titulo = titulo
    self.autor = autor
    self.paginas = paginas
    self.año_publicacion = año_publicacion
    self.disponible = disponible
    self.páginas_leídas = 0
    
    # Incrementar contador de libros
    Libro.cantidad_libros_creados += 1
```

**Línea por línea:**

```python
def __init__(self, titulo, autor, paginas, año_publicacion, disponible=True):
│    │        │    │     │     │       │         │            │
│    │        │    │     │     │       │         │            └─ Parámetro con valor por defecto
│    │        │    │     │     │       │         └─ Parámetro: cuando se publicó
│    │        │    │     │     │       └─ Parámetro: número de páginas
│    │        │    │     │     └─ Parámetro: quien escribió
│    │        │    │     └─ Parámetro: nombre del libro
│    │        │    └─ self: el objeto actual
│    │        └─ __init__: método constructor especial
│    └─ def: definir una función/método
└─ Los dos guiones indican que es un método especial
```

```python
self.titulo = titulo
```
- `self.titulo` = crear un atributo del objeto llamado "titulo"
- `= titulo` = asignarle el valor del parámetro

### Parte 4: Método para Obtener Información

```python
def obtener_información(self):
    """
    Método que retorna la información completa del libro
    """
    estado = "Disponible" if self.disponible else "No disponible"
    info = f"""
    ╔════════════════════════════════════╗
    ║        INFORMACIÓN DEL LIBRO       ║
    ╠════════════════════════════════════╣
    ║ Título: {self.titulo:<25} ║
    ...
    ╚════════════════════════════════════╝
    """
    return info
```

**Explicación:**
- `if self.disponible else` → Operador ternario (if corto)
- `f"""..."""` → f-string que permite insertar variables
- `{self.titulo:<25}` → Alinea el título a 25 caracteres
- `return info` → Retorna la cadena formateada

### Parte 5: Método para Simular Lectura

```python
def leer_páginas(self, cantidad_páginas):
    """
    Simula la lectura de un número de páginas
    """
    if not self.disponible:
        print("⚠️  El libro no está disponible para lectura.")
        return
    
    if cantidad_páginas <= 0:
        print("⚠️  Debe especificar un número válido de páginas.")
        return
    
    if self.páginas_leídas + cantidad_páginas > self.paginas:
        páginas_restantes = self.paginas - self.páginas_leídas
        print(f"⚠️  Solo hay {páginas_restantes} páginas restantes para leer.")
        print(f"✓ Se leyeron las {páginas_restantes} páginas restantes.")
        self.páginas_leídas = self.paginas
    else:
        self.páginas_leídas += cantidad_páginas
        print(f"✓ Se han leído {cantidad_páginas} páginas exitosamente.")
```

**Explicación:**
- Línea 1: Valida que el libro esté disponible
- Línea 2: Valida que la cantidad sea mayor a 0
- Línea 3: Valida que no se lean más páginas de las existentes
- Línea 4: Si todo es correcto, suma las páginas leídas

### Parte 6: Método para Mostrar Progreso

```python
def mostrar_progreso(self):
    """
    Muestra visualmente el progreso de lectura del libro
    """
    porcentaje = self.progreso_lectura()
    barra_longitud = 30
    relleno = int((porcentaje / 100) * barra_longitud)
    barra = "█" * relleno + "░" * (barra_longitud - relleno)
    
    print(f"\nProgreso de '{self.titulo}':")
    print(f"[{barra}] {porcentaje:.1f}% ({self.páginas_leídas}/{self.paginas})")
```

**Explicación:**
- Calcula el porcentaje de avance
- Crea una barra visual usando caracteres especiales
- `"█" * relleno` → Repite el carácter █ tantas veces como relleno
- `.1f` → Muestra 1 decimal (ej: 45.5%)

---

## Cómo se Usa el Programa

### Paso 1: Crear Objetos

```python
libro1 = Libro("El Quijote", "Miguel de Cervantes", 863, 1605)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 417, 1967)
libro3 = Libro("1984", "George Orwell", 328, 1949)
```

**¿Qué sucede?**
1. Se llama al constructor `__init__` 3 veces
2. Se crean 3 objetos diferentes
3. Cada objeto tiene sus propios atributos
4. El contador `cantidad_libros_creados` llega a 3

### Paso 2: Usar Métodos

```python
libro1.leer_páginas(100)      # Lee 100 páginas
libro1.leer_páginas(50)       # Lee 50 páginas más
libro1.mostrar_progreso()     # Muestra: [██████████░░░░░░░░] 17.4%
```

**¿Qué sucede?**
- Cada método actúa sobre el objeto específico
- Los atributos del objeto cambian
- Se muestra la información actualizada

### Paso 3: Comparar Objetos

```python
resultado = Libro.comparar_libros(libro1, libro2)
print(resultado)
# "'El Quijote' tiene más páginas (863)"
```

### Paso 4: Acceder a Información

```python
print(libro1.titulo)           # "El Quijote"
print(libro1.páginas_leídas)   # 150
print(Libro.cantidad_libros_creados)  # 3
```

---

## Flujo Completo de Ejecución

```
┌─────────────────────────────────────────┐
│ 1. Se define la clase Libro             │
│    - Atributos y métodos están listos   │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│ 2. Se crea libro1                       │
│    - Se ejecuta __init__()              │
│    - cantidad_libros_creados = 1        │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│ 3. Se crea libro2                       │
│    - Se ejecuta __init__()              │
│    - cantidad_libros_creados = 2        │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│ 4. Se llama libro1.leer_páginas(100)   │
│    - Se ejecuta el método               │
│    - página_leídas se actualiza         │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│ 5. Se llama libro1.mostrar_progreso()  │
│    - Calcula porcentaje                 │
│    - Muestra barra visual               │
└─────────────────────────────────────────┘
```

---

## Resumen de Conceptos Clave

| Concepto | Definición | Ejemplo |
|----------|-----------|---------|
| **Clase** | Molde o plantilla | `class Libro:` |
| **Objeto** | Instancia de una clase | `libro1 = Libro(...)` |
| **Atributo** | Propiedad/característica | `self.titulo` |
| **Método** | Función dentro de una clase | `def leer_páginas(self):` |
| **self** | Se refiere al objeto actual | `self.titulo = titulo` |
| **Constructor** | Método especial que inicia el objeto | `def __init__(self):` |
| **Encapsulación** | Agrupar datos y métodos relacionados | Todo en la clase Libro |

---

## Tips para Aprender POO

1. **Piensa en objetos reales** - ¿Qué atributos tiene? ¿Qué puede hacer?
2. **Usa `self` siempre** - Recuerda que actúas sobre un objeto específico
3. **Valida tu código** - Comprueba que los métodos funcionan con `print()`
4. **Experimenta** - Crea tus propias clases: Auto, Estudiante, Mascota, etc.
5. **Practica** - La repetición es la clave para entender POO

---

## Ejemplo Práctico: Crear tu Propia Clase

```python
class Automóvil:
    """Representa un automóvil"""
    
    cantidad_autos = 0
    
    def __init__(self, marca, modelo, año, velocidad_máxima):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad_máxima = velocidad_máxima
        self.velocidad_actual = 0
        Automóvil.cantidad_autos += 1
    
    def acelerar(self, incremento):
        """Aumenta la velocidad"""
        if self.velocidad_actual + incremento <= self.velocidad_máxima:
            self.velocidad_actual += incremento
            print(f"Velocidad: {self.velocidad_actual} km/h")
        else:
            print("¡Velocidad máxima alcanzada!")
    
    def frenar(self, decremento):
        """Disminuye la velocidad"""
        if self.velocidad_actual - decremento >= 0:
            self.velocidad_actual -= decremento
            print(f"Velocidad: {self.velocidad_actual} km/h")
        else:
            self.velocidad_actual = 0
            print("¡Auto detenido!")

# Usar la clase
mi_auto = Automóvil("Toyota", "Corolla", 2023, 180)
mi_auto.acelerar(50)  # Velocidad: 50 km/h
mi_auto.acelerar(60)  # Velocidad: 110 km/h
mi_auto.frenar(30)    # Velocidad: 80 km/h
print(Automóvil.cantidad_autos)  # 1
```

---

## ¡Conclusión!

Ahora entiendes los conceptos fundamentales de POO:
- ✅ Clases y objetos
- ✅ Atributos (de instancia y de clase)
- ✅ Métodos (instancia, estáticos, de clase)
- ✅ El constructor
- ✅ Cómo interactúan todos estos elementos

**Próximo paso:** Experimenta creando tus propias clases y modificando el código del programa de libros. ¡La práctica es la mejor manera de aprender!
