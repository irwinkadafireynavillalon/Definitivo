"""Validación de mediciones externas; no diagnostica ni controla hardware."""
from __future__ import annotations

from typing import Any

PROTOCOLO = "medicion-json-v1"


def validar_medicion(datos: dict[str, Any]) -> tuple[bool, list[str]]:
    errores: list[str] = []
    if datos.get("protocolo") != PROTOCOLO:
        errores.append(f"protocolo debe ser {PROTOCOLO}")
    medicion = datos.get("medicion")
    if not isinstance(medicion, dict):
        return False, errores + ["medicion debe ser un objeto"]
    muestras = medicion.get("muestras")
    if not isinstance(muestras, list) or not muestras:
        return False, errores + ["muestras debe ser una lista no vacía"]
    tiempo_anterior = -1
    for indice, muestra in enumerate(muestras):
        if not isinstance(muestra, dict):
            errores.append(f"muestras[{indice}] debe ser un objeto")
            continue
        tiempo = muestra.get("tiempo_ns")
        if isinstance(tiempo, bool) or not isinstance(tiempo, int) or tiempo < tiempo_anterior:
            errores.append(f"muestras[{indice}].tiempo_ns debe ser entero no decreciente")
        else:
            tiempo_anterior = tiempo
        for campo in ("voltaje_mv", "corriente_ma"):
            valor = muestra.get(campo)
            if valor is not None and (
                isinstance(valor, bool) or not isinstance(valor, (int, float)) or valor < 0
            ):
                errores.append(f"muestras[{indice}].{campo} debe ser no negativo o null")
    return not errores, errores


def estado_medicion(datos: dict[str, Any]) -> dict[str, Any]:
    valida, errores = validar_medicion(datos)
    medicion = datos.get("medicion", {}) if isinstance(datos, dict) else {}
    muestras = medicion.get("muestras", []) if isinstance(medicion, dict) else []
    calibrada = bool(medicion.get("id_calibracion")) if isinstance(medicion, dict) else False
    suficiente = valida and calibrada and len(muestras) >= 2
    return {
        "estado": "lista_para_revision_tecnica" if suficiente else "datos_insuficientes",
        "estructura_valida": valida, "calibrada": calibrada,
        "cantidad_muestras": len(muestras) if isinstance(muestras, list) else 0,
        "errores": errores, "diagnostico": None,
        "nota": "La corriente de entrada sola no confirma ni localiza un corto.",
    }
