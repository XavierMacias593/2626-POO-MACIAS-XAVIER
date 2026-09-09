import tkinter as tk
from tkinter import ttk


class MainView:
    """Vista principal del sistema con información actual del restaurante."""

    def __init__(self, root: tk.Tk, restaurante_servicio, on_logout) -> None:
        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.on_logout = on_logout

        self.frame = tk.Frame(self.root, bg="#ffffff")

        self.header = tk.Frame(self.frame, bg="#1f2937", padx=20, pady=15)
        self.header.pack(fill="x")

        tk.Label(
            self.header,
            text="Panel del restaurante",
            fg="white",
            bg="#1f2937",
            font=("Arial", 16, "bold"),
        ).pack(anchor="w")

        self.content = tk.Frame(self.frame, padx=20, pady=20, bg="#ffffff")
        self.content.pack(fill="both", expand=True)

        self.option_var = tk.StringVar(value="productos")
        self.tab_bar = ttk.Notebook(self.content)
        self.tab_bar.pack(fill="both", expand=True)

        self.productos_tab = tk.Frame(self.tab_bar, bg="#ffffff")
        self.usuarios_tab = tk.Frame(self.tab_bar, bg="#ffffff")
        self.ventas_tab = tk.Frame(self.tab_bar, bg="#ffffff")

        self.tab_bar.add(self.productos_tab, text="Productos")
        self.tab_bar.add(self.usuarios_tab, text="Usuarios")
        self.tab_bar.add(self.ventas_tab, text="Ventas")

        self._mostrar_productos()
        self._mostrar_usuarios()
        self._mostrar_ventas_pendientes()

        self.logout_button = tk.Button(
            self.frame,
            text="Cerrar sesión",
            command=self.on_logout,
            bg="#C62828",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=5,
        )
        self.logout_button.pack(pady=(0, 15))

    def _mostrar_productos(self) -> None:
        tk.Label(
            self.productos_tab,
            text="Productos registrados",
            font=("Arial", 12, "bold"),
            bg="#ffffff",
        ).pack(anchor="w", pady=(10, 5), padx=10)

        tree = ttk.Treeview(self.productos_tab, columns=("codigo", "nombre", "categoria", "precio", "stock"), show="headings")
        tree.heading("codigo", text="Código")
        tree.heading("nombre", text="Nombre")
        tree.heading("categoria", text="Categoría")
        tree.heading("precio", text="Precio")
        tree.heading("stock", text="Stock")
        tree.column("codigo", width=80)
        tree.column("nombre", width=180)
        tree.column("categoria", width=150)
        tree.column("precio", width=100)
        tree.column("stock", width=80)
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        for producto in self.restaurante_servicio.listar_productos():
            tree.insert(
                "",
                tk.END,
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    f"${producto.precio:.2f}",
                    producto.stock,
                ),
            )

    def _mostrar_usuarios(self) -> None:
        tk.Label(
            self.usuarios_tab,
            text="Usuarios registrados",
            font=("Arial", 12, "bold"),
            bg="#ffffff",
        ).pack(anchor="w", pady=(10, 5), padx=10)

        tree = ttk.Treeview(self.usuarios_tab, columns=("identificacion", "nombre", "correo"), show="headings")
        tree.heading("identificacion", text="Identificación")
        tree.heading("nombre", text="Nombre")
        tree.heading("correo", text="Correo")
        tree.column("identificacion", width=140)
        tree.column("nombre", width=200)
        tree.column("correo", width=220)
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        for usuario in self.restaurante_servicio.listar_usuarios():
            tree.insert("", tk.END, values=(usuario.identificacion, usuario.nombre, usuario.correo))

    def _mostrar_ventas_pendientes(self) -> None:
        tk.Label(
            self.ventas_tab,
            text="Ventas (pendiente)",
            font=("Arial", 12, "bold"),
            bg="#ffffff",
        ).pack(anchor="w", pady=(10, 5), padx=10)

        tk.Label(
            self.ventas_tab,
            text="La funcionalidad de ventas será desarrollada más adelante.",
            bg="#ffffff",
            fg="#555555",
            font=("Arial", 10),
        ).pack(anchor="w", padx=10, pady=20)

    def mostrar(self) -> None:
        self.frame.pack(fill="both", expand=True)

    def ocultar(self) -> None:
        self.frame.pack_forget()
