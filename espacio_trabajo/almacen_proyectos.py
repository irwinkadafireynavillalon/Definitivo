"""Lista los proyectos guardados en el espacio de trabajo."""
from pathlib import Path

CARPETA_PROYECTOS = Path(__file__).resolve().parent / "proyectos"


def listar_proyectos() -> list[str]:
    """Devuelve nombres de subcarpetas de proyectos, sin crear directorios."""
    if not CARPETA_PROYECTOS.is_dir():
        return []
    return sorted(ruta.name for ruta in CARPETA_PROYECTOS.iterdir() if ruta.is_dir())
