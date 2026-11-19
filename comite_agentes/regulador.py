"""
regulador.py — El refutador. Audita cualquier cosa ANTES de dártela por buena.
Regla de oro: si algo falla o se ve raro, lo detiene aquí, no deja que llegue a ti roto.
"""
import ast
from comite_agentes.estado import actualizar_estado

def auditar_codigo_python(codigo: str) -> dict:
    """Revisa que un código propuesto sea sintácticamente válido antes de guardarlo."""
    actualizar_estado("regulador", "auditando")
    try:
        ast.parse(codigo)
        actualizar_estado("regulador", "en_espera")
        return {"aprobado": True, "motivo": ""}
    except SyntaxError as e:
        actualizar_estado("regulador", "en_espera")
        return {"aprobado": False, "motivo": f"Error de sintaxis: {e}"}

def auditar_resultado_comando(exit_code: int, error: str) -> dict:
    """Revisa que un comando ejecutado haya salido bien de verdad."""
    actualizar_estado("regulador", "auditando")
    aprobado = (exit_code == 0 and not error)
    actualizar_estado("regulador", "en_espera")
    return {"aprobado": aprobado, "motivo": error if not aprobado else ""}
