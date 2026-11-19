"""
buscador_documentos.py — El que conecta con tus documentos/biblioteca (RAG).
Busca por significado, no por palabra exacta.
"""
from comite_agentes.estado import actualizar_estado

def buscar(consulta: str) -> list:
    actualizar_estado("buscador_documentos", "buscando")
    resultado = []  # pendiente de conectar con biblioteca/
    actualizar_estado("buscador_documentos", "en_espera")
    return resultado
