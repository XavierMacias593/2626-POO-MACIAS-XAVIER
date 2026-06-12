# Sistema de gestión de mascotas - Programación Tradicional


def registrar_mascota():
    nombre = input("Ingrese el nombre de la mascota: ").strip()
    especie = input("Ingrese la especie de la mascota: ").strip()
    edad = input("Ingrese la edad de la mascota: ").strip()

    return {
        "nombre": nombre,
        "especie": especie,
        "edad": edad,
    }


def mostrar_mascota(mascota):
    print("\n--- Información de la mascota ---")
    print(f"Nombre : {mascota['nombre']}")
    print(f"Especie: {mascota['especie']}")
    print(f"Edad   : {mascota['edad']}")
    print("--------------------------------")


def main():
    print("Sistema de gestión de mascotas (Programación Tradicional)")
    mascota = registrar_mascota()
    mostrar_mascota(mascota)


if __name__ == "__main__":
    main()
