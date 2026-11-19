"""
configuracion_orquestador.py
El orquestador es quien recibe lo que tú escribes y decide qué hacer:
platicar, buscar, ejecutar algo, o pedir ayuda a otra pieza del sistema.
Modo de comunicación: embebido (sin puertos, llamadas directas de función).
"""
from pathlib import Path
import sys

RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ_PROYECTO))

from ia_locales.configuracion_ia_local import modelos_disponibles

def estado_orquestador():
    """Revisa que el orquestador tenga a la mano lo que necesita para pensar."""
    return {
        "modelos_ia": modelos_disponibles(),
        "modo": "embebido",
    }
