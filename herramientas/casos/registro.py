"""Registro JSONL de casos; almacena fuera del repositorio."""
from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

CLAVES_RESTRINGIDAS = {
    "password", "token", "access_token", "customer_name", "nombre_cliente",
    "phone_number", "telefono", "email", "correo", "imei", "serial_number",
    "numero_serie",
}


def _revisar_privacidad(valor: Any, ruta: str = "caso") -> None:
    if isinstance(valor, dict):
        for clave, contenido in valor.items():
            if str(clave).casefold() in CLAVES_RESTRINGIDAS:
                raise ValueError(f"Campo privado no permitido: {ruta}.{clave}")
            _revisar_privacidad(contenido, f"{ruta}.{clave}")
    elif isinstance(valor, list):
        for indice, contenido in enumerate(valor):
            _revisar_privacidad(contenido, f"{ruta}[{indice}]")


def crear_caso(*, categoria: str, marca: str | None = None,
               modelo: str | None = None, sintomas: list[str] | None = None) -> dict[str, Any]:
    ahora = datetime.now(timezone.utc).isoformat()
    return {
        "id_caso": str(uuid.uuid4()), "creado": ahora, "actualizado": ahora,
        "categoria": categoria, "marca": marca, "modelo": modelo,
        "estado": "recibido", "sintomas": sintomas or [], "observaciones": [],
        "dispositivos": [], "fotos_privadas": [], "resultados": [],
        "aprobaciones": [], "notas": "",
    }


def agregar_dispositivo(caso: dict[str, Any], *, etiqueta: str, transporte: str,
                        fabricante_usb: str | None = None,
                        producto_usb: str | None = None) -> dict[str, Any]:
    dispositivo = {
        "id_dispositivo": str(uuid.uuid4()), "etiqueta": etiqueta,
        "transporte": transporte, "fabricante_usb": fabricante_usb,
        "producto_usb": producto_usb, "estado_conexion": "detectado",
    }
    _revisar_privacidad(dispositivo)
    caso.setdefault("dispositivos", []).append(dispositivo)
    caso["actualizado"] = datetime.now(timezone.utc).isoformat()
    return dispositivo


def agregar_referencia_foto(caso: dict[str, Any], ruta_privada_relativa: str,
                            descripcion: str = "") -> dict[str, Any]:
    """Guarda una referencia; la app debe capturar y guardar la imagen en privado."""
    ruta = Path(ruta_privada_relativa)
    if ruta.is_absolute() or ".." in ruta.parts or not ruta.as_posix().startswith("casos/"):
        raise ValueError("La foto debe estar bajo el directorio privado relativo 'casos/'.")
    referencia = {"id": str(uuid.uuid4()), "ruta": ruta.as_posix(),
                  "descripcion": descripcion, "almacenamiento": "privado_local"}
    caso.setdefault("fotos_privadas", []).append(referencia)
    return referencia


def guardar_caso(ruta: Path, caso: dict[str, Any]) -> None:
    """Añade un caso JSONL en la ubicación local indicada por el usuario."""
    _revisar_privacidad(caso)
    destino = Path(ruta)
    destino.parent.mkdir(parents=True, exist_ok=True)
    with destino.open("a", encoding="utf-8") as archivo:
        archivo.write(json.dumps(caso, ensure_ascii=False) + "\n")
