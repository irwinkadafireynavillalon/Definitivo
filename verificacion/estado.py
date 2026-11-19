"""estado.py — qué tan sana está la última revisión hecha."""
ESTADO_ACTUAL = {"ultima_revision": None, "aprobada": None}

def actualizar(aprobada: bool, detalle: str = ""):
    ESTADO_ACTUAL["ultima_revision"] = detalle
    ESTADO_ACTUAL["aprobada"] = aprobada
    return ESTADO_ACTUAL
