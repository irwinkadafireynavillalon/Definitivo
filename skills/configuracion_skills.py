"""Configuración central del subsistema de skills."""
from pathlib import Path

CARPETA_SKILLS = Path(__file__).resolve().parent
CARPETA_ACTIVAS = CARPETA_SKILLS / "activas"
CARPETA_RESERVA = CARPETA_SKILLS / "reserva_no_configuradas"
CARPETA_CATALOGO = CARPETA_SKILLS / "catalogo"
ARCHIVO_INDICE = CARPETA_CATALOGO / "indice.json"
ARCHIVO_COMPATIBILIDADES = CARPETA_CATALOGO / "compatibilidades.json"
ESTADO_CONEXION_INFERENCIA = "pendiente"
MAXIMO_CARACTERES_ENTRADA = 100_000
