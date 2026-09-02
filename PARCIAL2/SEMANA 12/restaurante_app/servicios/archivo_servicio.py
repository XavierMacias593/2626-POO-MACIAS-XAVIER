from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable, TypeVar

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

Modelo = TypeVar("Modelo")


class ArchivoServicio:
    """Centraliza la lectura y escritura de productos, usuarios y ventas."""

    def __init__(self, ruta_archivo: str | Path | None = None) -> None:
        ruta_productos = Path(ruta_archivo) if ruta_archivo else (
            Path(__file__).resolve().parent.parent / "datos" / "productos.json"
        )
        self.ruta_productos = ruta_productos
        self.ruta_usuarios = ruta_productos.with_name("usuarios.json")
        self.ruta_ventas = ruta_productos.with_name("ventas.json")

    def _cargar_registros(self, ruta: Path, nombre: str) -> list[dict[str, Any]]:
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                registros = json.load(archivo)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"Advertencia: {nombre} no contiene un JSON válido. Se iniciará vacío.")
            return []
        except PermissionError:
            print(f"Error: no hay permisos para leer {nombre}.")
            return []

        if not isinstance(registros, list):
            print(f"Advertencia: {nombre} debe contener una lista.")
            return []
        return [registro for registro in registros if isinstance(registro, dict)]

    def _cargar_modelos(
        self, ruta: Path, nombre: str, constructor: Callable[..., Modelo]
    ) -> list[Modelo]:
        modelos: list[Modelo] = []
        for indice, registro in enumerate(self._cargar_registros(ruta, nombre), start=1):
            try:
                modelos.append(constructor(**registro))
            except KeyError as error:
                print(f"Advertencia: se omitió el registro {indice}; falta la clave {error}.")
            except (TypeError, ValueError) as error:
                print(f"Advertencia: se omitió el registro {indice}: {error}.")
        return modelos

    def cargar_productos(self) -> list[Producto]:
        return self._cargar_modelos(self.ruta_productos, "productos.json", Producto)

    def cargar_usuarios(self) -> list[Usuario]:
        return self._cargar_modelos(self.ruta_usuarios, "usuarios.json", Usuario)

    def cargar_ventas(self) -> list[Venta]:
        return self._cargar_modelos(self.ruta_ventas, "ventas.json", Venta)

    def _guardar_registros(self, ruta: Path, registros: list[dict[str, Any]], nombre: str) -> None:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(registros, archivo, ensure_ascii=False, indent=4)
        except PermissionError as error:
            raise PermissionError(f"No hay permisos para escribir {nombre}.") from error

    def guardar_productos(self, productos: list[Producto]) -> None:
        self._guardar_registros(
            self.ruta_productos, [producto.to_dict() for producto in productos], "productos.json"
        )

    def guardar_usuarios(self, usuarios: list[Usuario]) -> None:
        self._guardar_registros(
            self.ruta_usuarios, [usuario.to_dict() for usuario in usuarios], "usuarios.json"
        )

    def guardar_ventas(self, ventas: list[Venta]) -> None:
        self._guardar_registros(
            self.ruta_ventas, [venta.to_dict() for venta in ventas], "ventas.json"
        )
