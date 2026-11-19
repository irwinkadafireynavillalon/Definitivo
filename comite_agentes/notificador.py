"""
notificador.py — El que te avisa a ti cuando algo importante pasa.
"""
from comite_agentes.estado import actualizar_estado

def avisar(mensaje: str) -> dict:
    actualizar_estado("notificador", "avisando")
    # Pendiente de conectar con las notificaciones reales de la app
    actualizar_estado("notificador", "en_espera")
    return {"enviado": True, "mensaje": mensaje}
