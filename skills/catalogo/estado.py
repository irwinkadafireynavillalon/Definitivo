"""Consulta de solo lectura al catálogo de skills."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

CARPETA_CATALOGO = Path(__file__).resolve().parent
ARCHIVO_INDICE = CARPETA_CATALOGO / "indice.json"
ARCHIVO_COMPATIBILIDADES = CARPETA_CATALOGO / "compatibilidades.json"


def _leer_json(ruta: Path) -> dict[str, Any]:
    """Lee un archivo JSON del catálogo y valida que su raíz sea un objeto."""
    with ruta.open("r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if not isinstance(datos, dict):
        raise ValueError(f"El catálogo debe contener un objeto: {ruta.name}")
    return datos


def listar_skills(estado: str | None = None) -> list[dict[str, Any]]:
    """Devuelve las entradas del índice, opcionalmente filtradas por estado."""
    datos = _leer_json(ARCHIVO_INDICE)
    skills = datos.get("skills", [])
    if not isinstance(skills, list):
        raise ValueError("El campo 'skills' debe ser una lista")
    entradas = [elemento for elemento in skills if isinstance(elemento, dict)]
    if estado is not None:
        entradas = [elemento for elemento in entradas if elemento.get("estado") == estado]
    return entradas


def obtener_compatibilidad(skill_id: str) -> dict[str, Any]:
    """Obtiene la compatibilidad declarada sin inferir conexiones no verificadas."""
    datos = _leer_json(ARCHIVO_COMPATIBILIDADES)
    compatibilidades = datos.get("compatibilidades", [])
    if not isinstance(compatibilidades, list):
        raise ValueError("El campo 'compatibilidades' debe ser una lista")
    for elemento in compatibilidades:
        if isinstance(elemento, dict) and elemento.get("skill_id") == skill_id:
            return elemento
    raise KeyError(f"No hay compatibilidad registrada para la skill: {skill_id}")
