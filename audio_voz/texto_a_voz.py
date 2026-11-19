"""
texto_a_voz.py
PENDIENTE: necesita un motor de texto-a-voz (ej. piper) que aun no
se ha descargado ni configurado.
"""
def hablar(texto: str) -> dict:
    return {"ok": False, "motivo": "motor de texto a voz no configurado todavia"}


def sintetizar(texto: str, salida: str | None = None) -> dict:
    """Prepara la solicitud local de síntesis de voz sin depender de red."""
    texto_limpio = str(texto).strip()
    if not texto_limpio:
        return {"ok": False, "error": "texto vacio", "ruta_audio": None}
    return {
        "ok": True,
        "texto": texto_limpio,
        "ruta_audio": salida,
        "pendiente_motor": True,
    }
