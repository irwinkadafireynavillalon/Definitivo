"""
metricas.py
Lee el registro real (no inventa numeros) y saca un resumen.
"""
import json
from pathlib import Path

ARCHIVO_REGISTRO = Path(__file__).resolve().parent / "actividad.jsonl"

def resumen() -> dict:
    if not ARCHIVO_REGISTRO.exists():
        return {"total": 0, "exitosos": 0, "fallidos": 0, "por_miembro": {}}
    total = exitosos = fallidos = 0
    por_miembro = {}
    with open(ARCHIVO_REGISTRO, "r", encoding="utf-8") as f:
        for linea in f:
            if not linea.strip():
                continue
            evento = json.loads(linea)
            total += 1
            if evento["exito"]:
                exitosos += 1
            else:
                fallidos += 1
            por_miembro.setdefault(evento["miembro"], 0)
            por_miembro[evento["miembro"]] += 1
    return {"total": total, "exitosos": exitosos, "fallidos": fallidos, "por_miembro": por_miembro}
