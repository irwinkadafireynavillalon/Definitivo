"""
configuracion_ia_local.py
Aquí se dice QUÉ modelo usar para CADA función, con nombres claros.
No hay que saber nada técnico — el nombre del archivo ya dice para qué sirve.
"""
from pathlib import Path

CARPETA_MODELOS = Path(__file__).resolve().parent / "modelos"

# "conversacion" = el modelo que platica contigo, responde preguntas
MODELO_CONVERSACION = CARPETA_MODELOS / "ia-conversacion.gguf"

# "entender_texto" = el modelo que entiende significado (para buscar en documentos, no palabra por palabra)
MODELO_ENTENDER_TEXTO = CARPETA_MODELOS / "ia-entender_texto.gguf"

# "imagen" = el modelo que crea o mejora imágenes
MODELO_IMAGEN = CARPETA_MODELOS / "ia-imagen.gguf"

# "video" = el modelo que crea o mejora videos
MODELO_VIDEO = CARPETA_MODELOS / "ia-video.gguf"

def modelos_disponibles():
    """Dice qué modelos ya están descargados y cuáles faltan."""
    return {
        "conversacion": MODELO_CONVERSACION.exists(),
        "entender_texto": MODELO_ENTENDER_TEXTO.exists(),
        "imagen": MODELO_IMAGEN.exists(),
        "video": MODELO_VIDEO.exists(),
    }
