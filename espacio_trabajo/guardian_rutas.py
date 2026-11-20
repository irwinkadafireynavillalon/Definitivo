"""Valida que las rutas de trabajo permanezcan dentro del repositorio."""
from pathlib import Path

RAIZ_PERMITIDA = Path(__file__).resolve().parent.parent


def ruta_segura(ruta: str | Path) -> dict:
    """Resuelve una ruta y rechaza escapes, rutas sensibles y el directorio Git."""
    candidata = Path(ruta)
    if not candidata.is_absolute():
        candidata = RAIZ_PERMITIDA / candidata
    resuelta = candidata.resolve()

    try:
        relativa = resuelta.relative_to(RAIZ_PERMITIDA)
    except ValueError:
        return {"segura": False, "motivo": "fuera de la carpeta del proyecto"}

    if ".git" in relativa.parts:
        return {"segura": False, "motivo": "no se permite acceder al directorio Git"}

    nombre = resuelta.name.casefold()
    if (nombre == ".env" or (nombre.startswith(".env.") and nombre != ".env.example")
            or resuelta.suffix.casefold() in {".key", ".pem"}):
        return {"segura": False, "motivo": "ruta de credenciales o clave privada bloqueada"}

    return {"segura": True, "ruta": str(resuelta)}
