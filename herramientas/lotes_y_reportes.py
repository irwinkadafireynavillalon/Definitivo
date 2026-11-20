"""Planes de diagnóstico por lotes; no ejecuta comandos ni accede a equipos."""
from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Any

COMPROBACIONES_LECTURA = {
    "inventario_usb", "estado_conexion", "revision_catalogo", "revision_manual"
}


def crear_plan_lote(dispositivos: list[dict[str, Any]],
                    comprobaciones: list[str]) -> dict[str, Any]:
    """Genera un plan pendiente de revisión por el técnico."""
    if not dispositivos:
        raise ValueError("El lote debe contener al menos un dispositivo.")
    no_admitidas = set(comprobaciones) - COMPROBACIONES_LECTURA
    if no_admitidas:
        raise ValueError(f"Comprobaciones no permitidas en un plan automático: {sorted(no_admitidas)}")
    if not comprobaciones:
        raise ValueError("Indica al menos una comprobación de solo lectura.")
    return {
        "id_lote": str(uuid.uuid4()),
        "creado": datetime.now(timezone.utc).isoformat(),
        "estado": "pendiente_revision",
        "ejecucion_iniciada": False,
        "comprobaciones": list(dict.fromkeys(comprobaciones)),
        "dispositivos": [
            {"id_dispositivo": equipo.get("id_dispositivo"),
             "etiqueta": equipo.get("etiqueta"), "estado": "pendiente"}
            for equipo in dispositivos
        ],
    }


def crear_aviso_local(evento: str, mensaje: str) -> dict[str, str]:
    """Crea datos para que la aplicación muestre un aviso local, si tiene permiso."""
    return {"id": str(uuid.uuid4()), "evento": evento, "mensaje": mensaje,
            "canal": "local", "creado": datetime.now(timezone.utc).isoformat()}


def crear_resumen(casos: list[dict[str, Any]]) -> dict[str, Any]:
    """Resume estados y resultados sin incluir fotos ni identificadores personales."""
    estados: dict[str, int] = {}
    resultados: dict[str, int] = {}
    for caso in casos:
        estado = str(caso.get("estado", "desconocido"))
        estados[estado] = estados.get(estado, 0) + 1
        for resultado in caso.get("resultados", []):
            etiqueta = str(resultado.get("estado", "pendiente"))
            resultados[etiqueta] = resultados.get(etiqueta, 0) + 1
    return {"cantidad_casos": len(casos), "estados": estados,
            "resultados": resultados, "incluye_datos_personales": False}
