"""
ia_local.py — El que piensa y responde usando el modelo de conversación.
"""
from comite_agentes.estado import actualizar_estado

def responder(pregunta: str) -> str:
    actualizar_estado("ia_local", "pensando")
    # Aquí se conectará con ia_locales/configuracion_ia_local.py cuando
    # tengamos el modelo cargado de verdad.
    actualizar_estado("ia_local", "en_espera")
    return f"(pendiente de conectar modelo real) respuesta a: {pregunta}"
