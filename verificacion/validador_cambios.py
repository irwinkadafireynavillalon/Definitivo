"""
validador_cambios.py
Revisa que un código propuesto cumpla las reglas del proyecto ANTES de guardarse:
- nombres en español, por función (no "app.py", "main.py", "sqlite_db.py")
- sin puertos ni IPs sueltas en el texto
"""
import re

NOMBRES_PROHIBIDOS = {"app.py", "main.py", "server.py", "index.py"}
PATRON_PUERTO_O_IP = re.compile(r"\b(127\.0\.0\.1|0\.0\.0\.0|localhost|:\d{4,5}\b)")

def validar(nombre_archivo: str, contenido: str) -> dict:
    problemas = []
    if nombre_archivo in NOMBRES_PROHIBIDOS:
        problemas.append(f"Nombre prohibido por convencion: {nombre_archivo}")
    if PATRON_PUERTO_O_IP.search(contenido):
        problemas.append("Se encontro IP o puerto en el codigo (proyecto es 'embebido', sin red)")
    return {"aprobado": len(problemas) == 0, "problemas": problemas}
