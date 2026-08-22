from __future__ import annotations

import json
from pathlib import Path

from modelos.producto import Producto


class ArchivoServicio:
    """Lee y escribe únicamente la colección persistente de productos."""

    def __init__(self, ruta_archivo: str | Path | None = None) -> None:
        self.ruta_archivo = Path(ruta_archivo) if ruta_archivo else (
            Path(__file__).resolve().parent.parent / "datos" / "productos.json"
        )

    def cargar_productos(self) -> list[Producto]:
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                registros = json.load(archivo)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"Advertencia: {self.ruta_archivo.name} no contiene un JSON válido. Se iniciará vacío.")
            return []
        except PermissionError:
            print(f"Error: no hay permisos para leer {self.ruta_archivo.name}.")
            return []

        if not isinstance(registros, list):
            print("Advertencia: productos.json debe contener una lista de productos.")
            return []

        productos: list[Producto] = []
        for indice, registro in enumerate(registros, start=1):
            try:
                if not isinstance(registro, dict):
                    raise ValueError("el registro no es un objeto JSON")
                producto = Producto(
                    registro["codigo"],
                    registro["nombre"],
                    registro["categoria"],
                    registro["precio"],
                )
                if any(item.codigo == producto.codigo for item in productos):
                    raise ValueError("el código está repetido")
                productos.append(producto)
            except KeyError as error:
                print(f"Advertencia: se omitió el registro {indice}; falta la clave {error}.")
            except (TypeError, ValueError) as error:
                print(f"Advertencia: se omitió el registro {indice}: {error}.")
        return productos

    def guardar_productos(self, productos: list[Producto]) -> None:
        self.ruta_archivo.parent.mkdir(parents=True, exist_ok=True)
        registros = [producto.to_dict() for producto in productos]
        try:
            with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(registros, archivo, ensure_ascii=False, indent=4)
        except PermissionError:
            raise PermissionError(f"No hay permisos para escribir {self.ruta_archivo.name}.")
