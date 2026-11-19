"""
estado.py — Aquí cada miembro del comité anota qué está haciendo ahorita.
Cualquier otra pieza del sistema puede preguntar "¿cómo va fulano?" sin adivinar.
"""
ESTADO_ACTUAL = {
    "orquestador": "en_espera",
    "ia_local": "en_espera",
    "buscador_documentos": "en_espera",
    "regulador": "en_espera",
    "constructor": "en_espera",
    "vigia": "en_espera",
    "notificador": "en_espera",
}

def actualizar_estado(miembro: str, nuevo_estado: str):
    if miembro in ESTADO_ACTUAL:
        ESTADO_ACTUAL[miembro] = nuevo_estado
    return ESTADO_ACTUAL
