"""
pruebas_automaticas.py
Compila CADA archivo .py del proyecto y reporta cuáles fallan.
No es un placeholder: de verdad recorre el proyecto y compila cada archivo.
"""
import py_compile
from pathlib import Path
from verificacion.estado import actualizar

RAIZ = Path(__file__).resolve().parent.parent

def ejecutar_pruebas() -> dict:
    archivos = [p for p in RAIZ.rglob("*.py") if "__pycache__" not in str(p)]
    fallos = []
    for archivo in archivos:
        try:
            py_compile.compile(str(archivo), doraise=True)
        except py_compile.PyCompileError as e:
            fallos.append({"archivo": str(archivo), "error": str(e)})
    aprobado = len(fallos) == 0
    actualizar(aprobado, f"{len(archivos)} archivos revisados, {len(fallos)} fallos")
    return {"total_revisados": len(archivos), "fallos": fallos, "aprobado": aprobado}
