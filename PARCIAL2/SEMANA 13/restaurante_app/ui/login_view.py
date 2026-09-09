import tkinter as tk
from tkinter import messagebox


class LoginView:
    """Vista de acceso a la aplicación del restaurante."""

    def __init__(self, root: tk.Tk, on_login_success, restaurante_servicio) -> None:
        self.root = root
        self.on_login_success = on_login_success
        self.restaurante_servicio = restaurante_servicio

        self.frame = tk.Frame(self.root, padx=30, pady=30, bg="#f5f5f5")
        self.frame.pack(fill="both", expand=True)

        self.title_label = tk.Label(
            self.frame,
            text="Restaurante App",
            font=("Arial", 20, "bold"),
            bg="#f5f5f5",
        )
        self.title_label.pack(pady=(0, 20))

        tk.Label(self.frame, text="Usuario", font=("Arial", 11), bg="#f5f5f5").pack(anchor="w")
        self.usuario_entry = tk.Entry(self.frame, width=30, font=("Arial", 11))
        self.usuario_entry.pack(pady=(5, 10), fill="x")

        tk.Label(self.frame, text="Contraseña", font=("Arial", 11), bg="#f5f5f5").pack(anchor="w")
        self.password_entry = tk.Entry(self.frame, width=30, show="*", font=("Arial", 11))
        self.password_entry.pack(pady=(5, 15), fill="x")

        self.login_button = tk.Button(
            self.frame,
            text="Ingresar",
            command=self.validar_credenciales,
            bg="#2E7D32",
            fg="white",
            font=("Arial", 11, "bold"),
            width=20,
        )
        self.login_button.pack(pady=10)

        self.mensaje_label = tk.Label(self.frame, text="", fg="red", bg="#f5f5f5")
        self.mensaje_label.pack()

    def validar_credenciales(self) -> None:
        usuario = self.usuario_entry.get().strip()
        password = self.password_entry.get().strip()

        if not usuario or not password:
            self.mensaje_label.config(text="Debe ingresar usuario y contraseña.")
            return

        if self.restaurante_servicio.validar_acceso(usuario, password):
            self.mensaje_label.config(text="")
            self.on_login_success()
        else:
            self.mensaje_label.config(text="Credenciales incorrectas.")
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def mostrar(self) -> None:
        self.frame.pack(fill="both", expand=True)

    def ocultar(self) -> None:
        self.frame.pack_forget()
