"""estado.py — registro de la última decisión de autorización."""
ESTADO_ACTUAL = {"ultima_accion": None, "autorizada": None}

def actualizar(accion: str, autorizada: bool):
    ESTADO_ACTUAL["ultima_accion"] = accion
    ESTADO_ACTUAL["autorizada"] = autorizada
    return ESTADO_ACTUAL
