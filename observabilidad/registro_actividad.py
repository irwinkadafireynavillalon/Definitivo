"""
registro_actividad.py
Guarda, de verdad, en un archivo, cada vez que un miembro del comite hace algo.
Se debe llamar desde comite_agentes/ en cada accion -- si nadie lo llama,
queda muerto igual que paso en el proyecto viejo. Esa es la advertencia.
"""
import json
import time
from pathlib import Path
from observabilidad.estado import incrementar

ARCHIVO_REGISTRO = Path(__file__).resolve().parent / "actividad.jsonl"

def registrar(miembro: str, accion: str, exito: bool, detalle: str = ""):
    evento = {
        "tiempo": time.strftime("%Y-%m-%d %H:%M:%S"),
        "miembro": miembro,
        "accion": accion,
        "exito": exito,
        "detalle": detalle,
    }
    with open(ARCHIVO_REGISTRO, "a", encoding="utf-8") as f:
        f.write(json.dumps(evento, ensure_ascii=False) + "\n")
    incrementar()
    return evento
