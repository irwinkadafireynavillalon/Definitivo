"""
orquestador.py (del comité) — Reparte el trabajo entre los demás miembros.
No piensa por sí mismo, decide A QUIÉN pasarle cada tarea.
"""
from comite_agentes.estado import actualizar_estado

def repartir_tarea(tipo_tarea: str):
    """Decide qué miembro del comité debe atender la tarea."""
    mapa = {
        "platica": "ia_local",
        "buscar_documento": "buscador_documentos",
        "construir_o_escribir": "constructor",
        "revisar_salud": "vigia",
    }
    responsable = mapa.get(tipo_tarea, "ia_local")
    actualizar_estado("orquestador", f"repartio_a_{responsable}")
    return responsable
