"""Evaluación segura de skills en reserva; nunca las activa ni las mueve."""
from __future__ import annotations

from skills.catalogo.estado import listar_skills


def proponer_evaluacion(skill_id: str) -> dict[str, str]:
    """Devuelve una propuesta para revisar una skill reservada, sin modificarla."""
    for skill in listar_skills():
        if skill.get("id") == skill_id and skill.get("estado") == "reserva":
            return {
                "estado": "pendiente_de_revision_y_confirmacion",
                "skill_id": skill_id,
                "motivo": "La skill permanece en reserva y no se carga automáticamente.",
            }
    raise KeyError(f"No se encontró una skill en reserva con id: {skill_id}")
