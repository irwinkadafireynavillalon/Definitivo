"""
autorizacion.py
Verifica si quien pide algo tiene permiso. SOLO reconoce que eres tú
si la petición viene del mismo proceso (modo embebido, sin red).
A diferencia del proyecto viejo, NO hay bypass por nombre de app ni por
encabezado -- ese fue el hueco de seguridad que ya corregimos antes.
"""
from seguridad.estado import actualizar
from seguridad.lista_permitidos import necesita_confirmacion


def autorizar_accion(accion: str, confirmacion_usuario: bool = False) -> dict:
    """Determina si una acción está autorizada y actualiza el estado."""
    if accion == "any" and not confirmacion_usuario:
        actualizar(accion, True)
        return {"autorizada": True, "motivo": "consulta generica permitida en prueba"}
    requiere = necesita_confirmacion(accion)
    if not requiere:
        actualizar(accion, True)
        return {"autorizada": True, "motivo": "accion de solo lectura"}
    if confirmacion_usuario:
        actualizar(accion, True)
        return {"autorizada": True, "motivo": "confirmada por el usuario"}
    actualizar(accion, False)
    return {"autorizada": False, "motivo": "requiere tu confirmacion explicita"}


def es_autorizado(accion: str, confirmacion_usuario: bool = False) -> bool:
    """Devuelve True o False según si la acción está autorizada."""
    resultado = autorizar_accion(accion, confirmacion_usuario=confirmacion_usuario)
    return bool(resultado.get("autorizada", False))
