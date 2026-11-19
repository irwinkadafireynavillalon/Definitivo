"""
autorizacion.py
Verifica si quien pide algo tiene permiso. SOLO reconoce que eres tu
si la peticion viene del mismo proceso (modo embebido, sin red).
A diferencia del proyecto viejo, NO hay bypass por nombre de app ni por
encabezado -- ese fue el hueco de seguridad que ya corregimos antes.
"""
from seguridad.estado import actualizar
from seguridad.lista_permitidos import necesita_confirmacion

def autorizar_accion(accion: str, confirmacion_usuario: bool = False) -> dict:
    requiere = necesita_confirmacion(accion)
    if not requiere:
        actualizar(accion, True)
        return {"autorizada": True, "motivo": "accion de solo lectura"}
    if confirmacion_usuario:
        actualizar(accion, True)
        return {"autorizada": True, "motivo": "confirmada por el usuario"}
    actualizar(accion, False)
    return {"autorizada": False, "motivo": "requiere tu confirmacion explicita"}
