# REGLAS DEL PROYECTO "DEFINITIVO" — OBLIGATORIAS

1. NOMBRES POR FUNCIÓN, NUNCA POR TECNOLOGÍA.
   - Mal: embeddings.gguf, sqlite_db.py, app.py, main.py
   - Bien: ia-entender_texto.gguf, memoria_rag.py, orquestador.py
   - Todo comentario y nombre de archivo en ESPAÑOL.

2. SIN PUERTOS NI IP. Modo de comunicación: "embebido" (llamadas de función
   directas, dentro del mismo proceso). Si una herramienta necesita red,
   decirlo explícito antes de programarla, no asumir puerto por default.

3. ANTES de pasar a la siguiente carpeta: correr
   `python3 -m py_compile archivo.py` en cada archivo nuevo o editado.
   Si falla, detenerse y arreglar ahí mismo. No seguir con error pendiente.

4. NUNCA reutilizar tokens, claves o nombres de proyectos anteriores
   (servidor_eterno, KDF, Kadafi, etc.) — este proyecto empieza limpio.

5. Antes de borrar o "optimizar" algo que ya existía en el proyecto,
   preguntar y esperar un "sí" explícito.

6. Seguir el orden de construcción ya decidido:
   configuracion.py (raíz) -> ia_locales/ -> orquestador/ -> comite_agentes/
   -> el resto de carpetas, una por una, sin saltar.
