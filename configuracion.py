"""
configuracion.py — Configuración global del proyecto Definitivo.
Todas las demás carpetas leen de aquí sus rutas y ajustes base.
"""
from pathlib import Path

RAIZ_PROYECTO = Path(__file__).resolve().parent
RAIZ_DATOS = RAIZ_PROYECTO / "datos"
RAIZ_DATOS.mkdir(exist_ok=True)

# Modo de comunicación interna: "embebido" (sin puertos), decidido ya
MODO_COMUNICACION = "embebido"

# Sin límite artificial de almacenamiento (solo el espacio real del dispositivo)
LIMITE_ALMACENAMIENTO_GB = None

def info_configuracion():
    return {
        "raiz": str(RAIZ_PROYECTO),
        "modo_comunicacion": MODO_COMUNICACION,
        "limite_almacenamiento": LIMITE_ALMACENAMIENTO_GB
    }
