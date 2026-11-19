"""
lista_permitidos.py
Reemplaza, con mejor diseño, lo que en el proyecto viejo era ALLOWED_COMMAND_BINARIES.
Separa acciones en 2 niveles: las que no necesitan preguntar, y las que SIEMPRE
necesitan tu "si" explicito, sin excepcion.
"""

SIN_PREGUNTAR = {
    "ver_hora", "ver_fecha", "ver_espacio_disco", "ver_memoria_libre",
    "listar_archivos", "leer_archivo_de_proyecto",
}

SIEMPRE_PREGUNTAR = {
    "instalar_paquete", "borrar_archivo", "ejecutar_comando_de_sistema",
    "escribir_archivo_nuevo", "modificar_archivo_existente",
    "usar_adb_o_fastboot", "acceso_root",
}

def necesita_confirmacion(accion: str) -> bool:
    if accion in SIN_PREGUNTAR:
        return False
    # Regla de oro: si no se reconoce la accion, se pregunta por seguridad.
    return True
