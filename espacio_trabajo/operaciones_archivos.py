"""Operaciones locales de archivos con rutas validadas y autorización."""
from pathlib import Path

from espacio_trabajo.guardian_rutas import ruta_segura
from seguridad.autorizacion import es_autorizado


def leer(ruta: str) -> dict:
    """Lee un archivo UTF-8 no sensible dentro del repositorio."""
    chequeo = ruta_segura(ruta)
    if not chequeo["segura"]:
        return {"ok": False, "motivo": chequeo["motivo"]}

    archivo = Path(chequeo["ruta"])
    if not archivo.is_file():
        return {"ok": False, "motivo": "no existe o no es un archivo regular"}

    try:
        return {"ok": True, "contenido": archivo.read_text(encoding="utf-8", errors="replace")}
    except OSError as error:
        return {"ok": False, "motivo": f"no se pudo leer el archivo: {error}"}


def escribir(ruta: str, contenido: str, confirmado: bool = False) -> dict:
    """Escribe solo tras confirmación explícita y sin crear carpetas implícitas."""
    chequeo = ruta_segura(ruta)
    if not chequeo["segura"]:
        return {"ok": False, "motivo": chequeo["motivo"]}

    archivo = Path(chequeo["ruta"])
    if archivo.exists() and not archivo.is_file():
        return {"ok": False, "motivo": "el destino existe y no es un archivo regular"}
    if not archivo.parent.is_dir():
        return {"ok": False, "motivo": "la carpeta de destino no existe"}

    accion = "modificar_archivo_existente" if archivo.exists() else "escribir_archivo_nuevo"
    if not es_autorizado(accion, confirmacion_usuario=confirmado):
        return {"ok": False, "motivo": "pendiente de confirmación explícita del usuario"}

    try:
        archivo.write_text(contenido, encoding="utf-8")
    except OSError as error:
        return {"ok": False, "motivo": f"no se pudo escribir el archivo: {error}"}
    return {"ok": True, "ruta": str(archivo)}
