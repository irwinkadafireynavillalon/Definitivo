"""
grabar_voz.py
PENDIENTE: necesita una libreria de grabacion (ej. sounddevice o termux-api).
Esta funcion existe para que el resto del sistema ya pueda llamarla,
pero hoy regresa un error honesto en vez de fingir que grabo algo.
"""
def grabar(duracion_segundos: int = 5) -> dict:
    return {"ok": False, "motivo": "libreria de audio no instalada todavia"}
