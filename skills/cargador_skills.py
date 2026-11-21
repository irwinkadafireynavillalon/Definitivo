"""Carga bajo demanda y prepara skills para un adaptador de inferencia local."""
from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Any

from skills.catalogo.estado import listar_skills, obtener_compatibilidad
from skills.configuracion_skills import CARPETA_SKILLS, MAXIMO_CARACTERES_ENTRADA

FuncionInferencia = Callable[[str, str], str]


def _buscar_skill_activa(skill_id: str) -> dict[str, Any]:
    """Encuentra una skill activa sin aceptar rutas indicadas por el llamador."""
    for skill in listar_skills(estado="activa_preparada"):
        if skill.get("id") == skill_id:
            return skill
    raise KeyError(f"La skill no existe o no está activa: {skill_id}")


def cargar_skill(skill_id: str) -> dict[str, Any]:
    """Carga únicamente las instrucciones de la skill activa solicitada."""
    skill = _buscar_skill_activa(skill_id)
    ruta_relativa = skill.get("archivo")
    if not isinstance(ruta_relativa, str):
        raise ValueError("La skill no tiene una ruta válida en el catálogo")
    ruta = (CARPETA_SKILLS / ruta_relativa).resolve()
    try:
        ruta.relative_to(CARPETA_SKILLS.resolve())
    except ValueError as error:
        raise ValueError("La ruta de la skill debe permanecer dentro de skills/") from error
    if not ruta.is_file():
        raise FileNotFoundError(f"No existe el archivo de instrucciones: {ruta_relativa}")
    instrucciones = ruta.read_text(encoding="utf-8")
    return {"skill": skill, "instrucciones": instrucciones}


def preparar_solicitud(skill_id: str, entrada: str) -> dict[str, Any]:
    """Prepara instrucciones y datos para inferencia; no invoca ni simula un modelo."""
    if not isinstance(entrada, str):
        raise TypeError("La entrada de la skill debe ser texto")
    if len(entrada) > MAXIMO_CARACTERES_ENTRADA:
        raise ValueError("La entrada supera el máximo permitido para esta skill")
    cargada = cargar_skill(skill_id)
    compatibilidad = obtener_compatibilidad(skill_id)
    solicitud = (
        f"Instrucciones de la skill:\n{cargada['instrucciones']}\n\n"
        f"Contenido proporcionado para la tarea:\n{entrada}"
    )
    return {
        "estado": "preparada_pendiente_de_inferencia",
        "skill_id": skill_id,
        "modelo_local": compatibilidad.get("modelo_local"),
        "estado_conexion": compatibilidad.get("estado_conexion"),
        "solicitud": solicitud,
    }


def ejecutar_skill(
    skill_id: str,
    entrada: str,
    invocar_modelo: FuncionInferencia | None = None,
) -> dict[str, Any]:
    """Envía la solicitud al adaptador proporcionado o informa que falta conectarlo."""
    preparada = preparar_solicitud(skill_id, entrada)
    if invocar_modelo is None:
        return preparada
    modelo = preparada["modelo_local"]
    respuesta = invocar_modelo(modelo, preparada["solicitud"])
    return {
        "estado": "respuesta_recibida",
        "skill_id": skill_id,
        "modelo_local": modelo,
        "respuesta": respuesta,
    }
