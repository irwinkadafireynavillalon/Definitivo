"""estado.py — cuantos eventos se han registrado hasta ahora."""
ESTADO_ACTUAL = {"eventos_registrados": 0}

def incrementar():
    ESTADO_ACTUAL["eventos_registrados"] += 1
    return ESTADO_ACTUAL
