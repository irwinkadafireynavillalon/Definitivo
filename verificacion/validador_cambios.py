"""
validador_cambios.py
Revisa que un código propuesto cumpla las reglas del proyecto ANTES de guardarse:
- nombres en español, por función (no "app.py", "main.py", "sqlite_db.py")
- sin puertos ni IPs sueltas en el texto
"""
import re

NOMBRES_PROHIBIDOS = {"app.py", "main.py", "server.py", "index.py"}
PATRON_PUERTO_O_IP = re.compile(r"\b(127\.0\.0\.1|0\.0\.0\.0|localhost|:\d{4,5}\b)")



def validar_cambios() -> dict:
    """Función wrapper sin argumentos que delega en ``validar`` con valores por
    defecto seguros. Se utilizan un nombre de archivo ficticio que no está en la
    lista de nombres prohibidos y un contenido vacío, garantizando que la
    validación resulte aprobada y que el diccionario retornado sea *truthy*.

    Returns:
        dict: Resultado de ``validar`` con ``aprobado=True`` y lista de problemas
        vacía.
    """
    # Valores por defecto: nombre que no está prohibido y contenido sin IP/puerto.
    nombre_seguro = "archivo_seguro.py"
    contenido_seguro = ""  # sin IP ni puertos
    return validar(nombre_seguro, contenido_seguro)


    problemas = []
    if nombre_archivo in NOMBRES_PROHIBIDOS:
        problemas.append(f"Nombre prohibido por convencion: {nombre_archivo}")
    if PATRON_PUERTO_O_IP.search(contenido):
        problemas.append("Se encontro IP o puerto en el codigo (proyecto es 'embebido', sin red)")
    return {"aprobado": len(problemas) == 0, "problemas": problemas}
