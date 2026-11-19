"""
constructor.py — El que ejecuta acciones o escribe código/archivos.
Todo lo que construya debe pasar por regulador.py antes de darse por bueno.
"""
from comite_agentes.estado import actualizar_estado
from comite_agentes.regulador import auditar_codigo_python

def proponer_archivo_nuevo(ruta: str, contenido: str) -> dict:
    actualizar_estado("constructor", "construyendo")
    auditoria = auditar_codigo_python(contenido)
    actualizar_estado("constructor", "en_espera")
    if not auditoria["aprobado"]:
        return {"guardado": False, "motivo": auditoria["motivo"]}
    return {"guardado": False, "motivo": "pendiente de confirmacion del usuario", "ruta": ruta, "contenido": contenido}
