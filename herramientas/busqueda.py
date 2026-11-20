"""Búsqueda local de herramientas candidatas, sin ejecutar programas."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

RUTA_CATALOGO = Path(__file__).with_name("herramientas.json")


def cargar_catalogo(ruta: Path = RUTA_CATALOGO) -> dict[str, Any]:
    """Carga el catálogo y comprueba su estructura mínima."""
    with Path(ruta).open(encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if not isinstance(datos, dict) or not isinstance(datos.get("herramientas"), list):
        raise ValueError("El catálogo debe tener una lista 'herramientas'.")
    return datos


def buscar_herramientas(
    catalogo: dict[str, Any], *, categoria: str | None = None,
    marca: str | None = None, modelo: str | None = None,
    protocolo: str | None = None, chipset: str | None = None,
) -> list[dict[str, Any]]:
    """Devuelve candidatos; el texto de modelo nunca confirma compatibilidad."""
    resultados = []
    for herramienta in catalogo.get("herramientas", []):
        if categoria and categoria not in herramienta.get("categorias", []):
            continue
        marcas = herramienta.get("marcas", [])
        if marca and marcas and not any(
            marca.casefold() in str(valor).casefold()
            for valor in marcas + ["Universal"]
        ):
            continue
        if protocolo and not any(
            protocolo.casefold() in str(valor).casefold()
            for valor in herramienta.get("protocolos", [])
        ):
            continue
        if chipset and not any(
            chipset.casefold() in str(valor).casefold()
            for valor in herramienta.get("chipsets", [])
        ):
            continue
        candidato = dict(herramienta)
        if modelo:
            candidato["compatibilidad_modelo"] = "no_confirmada"
        resultados.append(candidato)
    return resultados


def validar_catalogo(catalogo: dict[str, Any]) -> list[str]:
    """Detecta IDs vacíos o repetidos sin modificar el catálogo."""
    errores = []
    vistos: set[str] = set()
    for indice, elemento in enumerate(catalogo.get("herramientas", [])):
        identificador = elemento.get("id") if isinstance(elemento, dict) else None
        if not isinstance(identificador, str) or not identificador.strip():
            errores.append(f"herramientas[{indice}] requiere id")
        elif identificador in vistos:
            errores.append(f"id duplicado: {identificador}")
        else:
            vistos.add(identificador)
    return errores
