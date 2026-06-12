from mascota import Mascota


def main():
    mascota1 = Mascota(nombre="Luna", especie="Perro", edad=3)
    mascota2 = Mascota(nombre="Milo", especie="Gato", edad=2)

    mascotas = [mascota1, mascota2]

    for mascota in mascotas:
        mascota.mostrar_informacion()
        mascota.hacer_sonido()
        print()


if __name__ == "__main__":
    main()
