import tkinter as tk

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class App:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Restaurante App")
        self.root.geometry("900x600")
        self.root.minsize(700, 500)

        self.archivo_servicio = ArchivoServicio()
        self.restaurante_servicio = RestauranteServicio(self.archivo_servicio)

        self.login_view = LoginView(root, self.mostrar_main_view, self.restaurante_servicio)
        self.main_view = MainView(root, self.restaurante_servicio, self.mostrar_login_view)

        self.mostrar_login_view()

    def mostrar_login_view(self) -> None:
        self.main_view.ocultar()
        self.login_view.mostrar()
        self.root.title("Restaurante App - Login")

    def mostrar_main_view(self) -> None:
        self.login_view.ocultar()
        self.main_view.mostrar()
        self.root.title("Restaurante App - Inicio")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
