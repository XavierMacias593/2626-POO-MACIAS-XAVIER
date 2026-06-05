# ============================================================================
# TAREA SEMANA 2 - PROGRAMACIÓN ORIENTADA A OBJETOS
# Autor: Xavier Macías
# Descripción: Programa básico que representa un Libro como objeto real
#              utilizando una clase en Python
# ============================================================================

class Libro:
    """
    Clase que representa un libro con sus atributos y métodos.
    Un libro es un ejemplo de objeto del mundo real que tiene propiedades
    y comportamientos que podemos modelar en código.
    """
    
    # Atributo de clase (compartido por todas las instancias)
    cantidad_libros_creados = 0
    
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
        self.páginas_leídas = 0  # Por defecto, no se ha leído nada
        
        # Incrementar contador de libros
        Libro.cantidad_libros_creados += 1
    
    def obtener_información(self):
        """
        Método que retorna la información completa del libro
        
        Retorna:
            str: Una cadena con todos los detalles del libro
        """
        estado = "Disponible" if self.disponible else "No disponible"
        info = f"""
        ╔════════════════════════════════════╗
        ║        INFORMACIÓN DEL LIBRO       ║
        ╠════════════════════════════════════╣
        ║ Título: {self.titulo:<25} ║
        ║ Autor: {self.autor:<26} ║
        ║ Páginas: {self.paginas:<23} ║
        ║ Año: {self.año_publicacion:<27} ║
        ║ Estado: {estado:<25} ║
        ║ Páginas leídas: {self.páginas_leídas:<17} ║
        ╚════════════════════════════════════╝
        """
        return info
    
    def leer_páginas(self, cantidad_páginas):
        """
        Simula la lectura de un número de páginas
        
        Parámetros:
            cantidad_páginas (int): Número de páginas a leer
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
    
    def progreso_lectura(self):
        """
        Retorna el porcentaje de avance en la lectura del libro
        
        Retorna:
            float: Porcentaje de avance
        """
        if self.paginas == 0:
            return 0
        return (self.páginas_leídas / self.paginas) * 100
    
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
    
    def cambiar_disponibilidad(self, disponible):
        """
        Cambia el estado de disponibilidad del libro
        
        Parámetros:
            disponible (bool): True si está disponible, False si no
        """
        self.disponible = disponible
        estado = "Ahora está disponible" if disponible else "Ahora no está disponible"
        print(f"✓ {estado}")
    
    def completar_lectura(self):
        """
        Marca el libro como completamente leído
        """
        self.páginas_leídas = self.paginas
        print(f"✓ ¡Felicidades! Has completado '{self.titulo}'")
    
    def reiniciar_lectura(self):
        """
        Reinicia el contador de páginas leídas
        """
        self.páginas_leídas = 0
        print(f"✓ Lectura de '{self.titulo}' reiniciada")
    
    @staticmethod
    def comparar_libros(libro1, libro2):
        """
        Método estático que compara dos libros por número de páginas
        
        Parámetros:
            libro1: Primer libro
            libro2: Segundo libro
        """
        if libro1.paginas > libro2.paginas:
            return f"'{libro1.titulo}' tiene más páginas ({libro1.paginas})"
        elif libro1.paginas < libro2.paginas:
            return f"'{libro2.titulo}' tiene más páginas ({libro2.paginas})"
        else:
            return f"Ambos libros tienen la misma cantidad de páginas ({libro1.paginas})"
    
    @classmethod
    def obtener_cantidad_libros(cls):
        """
        Método de clase que retorna la cantidad total de libros creados
        
        Retorna:
            int: Número total de libros
        """
        return cls.cantidad_libros_creados
    
    def __str__(self):
        """
        Método especial para representar el objeto como cadena
        """
        return f"'{self.titulo}' por {self.autor}"
    
    def __repr__(self):
        """
        Método especial para representación técnica del objeto
        """
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', paginas={self.paginas})"


# ============================================================================
# PROGRAMA PRINCIPAL - Demostraciones y pruebas
# ============================================================================

def main():
    print("=" * 50)
    print("SISTEMA DE GESTIÓN DE LIBROS")
    print("=" * 50)
    
    # Crear instancias de la clase Libro
    print("\n1️⃣  CREANDO LIBROS...\n")
    
    libro1 = Libro("El Quijote", "Miguel de Cervantes", 863, 1605)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 417, 1967)
    libro3 = Libro("1984", "George Orwell", 328, 1949)
    
    print(f"✓ Se han creado {Libro.obtener_cantidad_libros()} libros")
    
    # Mostrar información de los libros
    print(libro1.obtener_información())
    
    # Simular lectura
    print("\n2️⃣  SIMULANDO LECTURA...\n")
    libro1.leer_páginas(100)
    libro1.leer_páginas(50)
    libro1.mostrar_progreso()
    
    # Intentar leer más páginas de las disponibles
    print("\n3️⃣  INTENTANDO LEER MÁS PÁGINAS DE LAS DISPONIBLES...\n")
    libro1.leer_páginas(1000)
    
    # Completar lectura
    print("\n4️⃣  COMPLETANDO LECTURA...\n")
    libro1.completar_lectura()
    libro1.mostrar_progreso()
    
    # Cambiar disponibilidad
    print("\n5️⃣  CAMBIANDO DISPONIBILIDAD...\n")
    libro1.cambiar_disponibilidad(False)
    
    # Intentar leer un libro no disponible
    print()
    libro1.leer_páginas(10)
    
    # Comparar libros
    print("\n6️⃣  COMPARANDO LIBROS...\n")
    comparacion = Libro.comparar_libros(libro1, libro2)
    print(f"  → {comparacion}")
    
    comparacion2 = Libro.comparar_libros(libro2, libro3)
    print(f"  → {comparacion2}")
    
    # Mostrar información de otros libros
    print("\n7️⃣  INFORMACIÓN DE OTROS LIBROS...\n")
    print(f"  Libro 2: {libro2}")
    print(f"  Libro 3: {libro3}")
    print(f"  Representación técnica: {repr(libro2)}")
    
    # Simular lectura en libro2
    print("\n8️⃣  SIMULANDO LECTURA EN LIBRO2...\n")
    libro2.leer_páginas(150)
    libro2.mostrar_progreso()
    
    # Reiniciar lectura
    print("\n9️⃣  REINICIANDO LECTURA EN LIBRO2...\n")
    libro2.reiniciar_lectura()
    libro2.mostrar_progreso()
    
    # Resumen final
    print("\n🔟 RESUMEN FINAL...\n")
    print(f"  Total de libros creados: {Libro.obtener_cantidad_libros()}")
    print(f"  Porcentaje de lectura - Libro 1: {libro1.progreso_lectura():.1f}%")
    print(f"  Porcentaje de lectura - Libro 2: {libro2.progreso_lectura():.1f}%")
    print(f"  Porcentaje de lectura - Libro 3: {libro3.progreso_lectura():.1f}%")
    
    print("\n" + "=" * 50)
    print("¡PROGRAMA FINALIZADO!")
    print("=" * 50)


# Ejecutar el programa principal
if __name__ == "__main__":
    main()
