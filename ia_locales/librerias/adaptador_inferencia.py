"""Adaptador explícito para conectar un motor de inferencia local."""
from __future__ import annotations

from collections.abc import Callable

MotorInferencia = Callable[[str, str], str]


def crear_adaptador(motor: MotorInferencia) -> MotorInferencia:
    """Valida y devuelve un adaptador para un motor inyectado por la aplicación."""
    if not callable(motor):
        raise TypeError("El motor de inferencia debe ser una función invocable")

    def invocar(nombre_modelo: str, solicitud: str) -> str:
        if not nombre_modelo or not isinstance(nombre_modelo, str):
            raise ValueError("Debe indicarse un nombre de modelo compatible")
        if not isinstance(solicitud, str):
            raise TypeError("La solicitud de inferencia debe ser texto")
        respuesta = motor(nombre_modelo, solicitud)
        if not isinstance(respuesta, str):
            raise TypeError("El motor debe devolver una respuesta de texto")
        return respuesta

    return invocar
