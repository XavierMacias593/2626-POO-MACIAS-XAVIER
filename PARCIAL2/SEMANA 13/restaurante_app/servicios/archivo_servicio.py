import json
from pathlib import Path
from typing import Any, TypeVar, Callable

from modelos.producto import Producto
from modelos.usuario import Usuario

Modelo = TypeVar("Modelo")


class ArchivoServicio:
    """Carga y guarda la información persistida en archivos JSON."""

    def __init__(self, ruta_base: str | Path | None = None) -> None:
        if ruta_base is None:
            ruta_base = Path(__file__).resolve().parent.parent / "datos"
        self.ruta_base = Path(ruta_base)
        self.ruta_productos = self.ruta_base / "productos.json"
        self.ruta_usuarios = self.ruta_base / "usuarios.json"

    def _leer_json(self, ruta: Path) -> list[dict[str, Any]]:
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
            if not isinstance(datos, list):
                return []
            return [item for item in datos if isinstance(item, dict)]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def _cargar_modelos(self, ruta: Path, constructor: Callable[..., Modelo]) -> list[Modelo]:
        modelos: list[Modelo] = []
        for item in self._leer_json(ruta):
            try:
                modelos.append(constructor(**item))
            except (TypeError, ValueError):
                continue
        return modelos

    def cargar_productos(self) -> list[Producto]:
        return self._cargar_modelos(self.ruta_productos, Producto)

    def cargar_usuarios(self) -> list[Usuario]:
        return self._cargar_modelos(self.ruta_usuarios, Usuario)
