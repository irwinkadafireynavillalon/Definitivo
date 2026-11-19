# TAREA PARA ANTIGRAVITY — Mientras Claude no tiene tokens

Antes de hacer CUALQUIER cosa: lee `~/definitivo/REGLAS_DEFINITIVO.md`
y síguelo al pie de la letra. Resumen de lo que ya debes saber:
- Nombres de archivos y comentarios EN ESPAÑOL, por función, nunca por
  tecnología (ej: "memoria_rag.py", no "sqlite_db.py").
- Modo de comunicación: EMBEBIDO, sin puertos, sin IPs. Nada de 127.0.0.1
  ni números de puerto en ningún archivo nuevo.
- Después de CADA archivo .py que crees, corre
  `python3 -m py_compile archivo.py` antes de seguir con el siguiente.
  Si falla, detente y arréglalo ahí mismo.
- NUNCA borres ni "optimices" nada que ya exista sin preguntar primero.
- Al terminar cada carpeta completa, haz commit y push a GitHub
  (el repo ya está configurado en ~/definitivo, remoto "origin").

## Carpetas a crear, EN ESTE ORDEN (no saltar ninguna):

### 1. verificacion/
Archivos: `pruebas_automaticas.py`, `validador_cambios.py`, `estado.py`
Función: antes de que el constructor del comité de agentes dé algo por
guardado, aquí se corre una prueba real (no solo sintaxis, sino que el
código haga lo que dice que hace). Debe poder importar y usar
`comite_agentes/regulador.py` como apoyo, no reemplazarlo.

### 2. seguridad/
Archivos: `lista_permitidos.py` (qué acciones puede hacer el sistema sin
preguntar, y cuáles necesitan tu "sí"), `autorizacion.py`, `estado.py`.
Debe reemplazar, con mejor diseño, lo que en el proyecto viejo
(servidor_eterno) se llamaba ALLOWED_COMMAND_BINARIES e is_master_authorized.

### 3. observabilidad/
Archivos: `registro_actividad.py` (guarda qué hizo cada miembro del comité
y cuándo), `metricas.py`, `estado.py`. Debe ser llamado de verdad desde
`comite_agentes/` cada vez que algo se ejecuta — NO debe quedar como
código muerto que nadie invoca (ese fue el error del proyecto viejo).

### 4. audio_voz/
Archivos: `grabar_voz.py`, `transcribir_a_texto.py`, `texto_a_voz.py`,
`estado.py`. Sin interfaz visual todavía, solo las funciones base.

### 5. orquestador/nix_droid/ (YA EXISTE LA CARPETA, falta el contenido)
Archivo: `gestor_paquetes.py` — administra instalación de paquetes usando
nix-on-droid como motor, PERO siempre con el mismo flujo de "propón,
espera la confirmación del usuario, luego instala" que ya usa
`comite_agentes/constructor.py`. Nunca instala nada sin preguntar primero.
Archivo: `estado.py`

## Al terminar TODO:
Corre `git log --oneline -5` y pégamelo cuando yo regrese, junto con
cualquier error que haya salido en el camino (sin esconder ninguno).
