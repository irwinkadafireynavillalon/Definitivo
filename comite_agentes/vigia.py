"""
vigia.py — Revisa que todo el sistema siga vivo y funcionando.
"""
from comite_agentes.estado import ESTADO_ACTUAL, actualizar_estado

def revisar_salud() -> dict:
    actualizar_estado("vigia", "revisando")
    reporte = dict(ESTADO_ACTUAL)
    actualizar_estado("vigia", "en_espera")
    return reporte
