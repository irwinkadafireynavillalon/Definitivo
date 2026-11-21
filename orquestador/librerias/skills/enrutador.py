"""Puente interno entre el orquestador y el cargador central de skills."""
from __future__ import annotations

from collections.abc import Callable
from typing import Any

from skills.cargador_skills import ejecutar_skill

FuncionInferencia = Callable[[str, str], str]

MAPA_SKILLS_POR_TAREA = {
    "leer_txt": "lectura_txt",
    "comprender_documento": "lectura_txt",
}


def ejecutar_tarea(
    tipo_tarea: str,
    contenido: str,
    invocar_modelo: FuncionInferencia | None = None,
) -> dict[str, Any]:
    """Enruta solo tareas conocidas al catálogo central, sin cargar otras skills."""
    skill_id = MAPA_SKILLS_POR_TAREA.get(tipo_tarea)
    if skill_id is None:
        return {"estado": "sin_skill_asignada", "tipo_tarea": tipo_tarea}
    return ejecutar_skill(skill_id, contenido, invocar_modelo=invocar_modelo)
