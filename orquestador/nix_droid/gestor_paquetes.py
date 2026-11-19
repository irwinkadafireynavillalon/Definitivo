"""
gestor_paquetes.py
Mismo flujo que comite_agentes/constructor.py: PROPONE, nunca instala solo.
"""
from orquestador.nix_droid.estado import ESTADO_ACTUAL

def proponer_instalacion(paquete: str) -> dict:
    ESTADO_ACTUAL["ultima_propuesta"] = paquete
    return {
        "instalado": False,
        "motivo": "pendiente de confirmacion del usuario",
        "paquete": paquete,
    }
