# Documento maestro de arquitectura de sistemas e inteligencia artificial (2026)

**Proyecto:** AINEK Neural Computer (ANC Team) / Definitivo  
**Estado:** Documento de arquitectura objetivo. La presencia de un módulo en este documento no implica que ya esté implementado.

---

## Tabla de contenido

1. Visión general y principios de diseño
2. Equipo de agentes ANC Team
3. Capas del ecosistema e infraestructura de IA
4. Catálogo funcional de herramientas de IA
5. Arquitectura de directorios y módulos
6. Flujo de ejecución, auditoría y seguridad
7. Datos locales y monitoreo regional (Mi Zona)
8. Protocolos de ejecución y gestión de paquetes (Nix-on-Droid)
9. Estado actual y criterios de implementación

---

## 1. Visión general y principios de diseño

AINEK Neural Computer (ANC) se plantea como un sistema modular híbrido —local y nube— para entornos móviles y Linux, incluidos Termux, Nix-on-Droid y PRoot. La ejecución debe ser supervisada, con permisos mínimos y separación clara entre propuestas y acciones efectivas.

### Principios rectores

1. **Cero caos:** separar planificación, construcción, supervisión, refutación y verificación.
2. **Local primero:** consultar primero la información y los modelos disponibles localmente. Usar servicios externos solo cuando sean necesarios y se haya informado al usuario.
3. **Confirmación explícita:** instalaciones, operaciones privilegiadas, cambios de sistema y otras acciones sensibles requieren una aprobación clara y específica antes de ejecutarse.
4. **Auditoría cruzada:** revisar resultados y cambios con políticas de seguridad y pruebas automatizadas. La revisión de un agente no sustituye pruebas ni autorización del usuario.
5. **Privacidad por diseño:** minimizar datos, almacenar información local de forma privada y no recopilar datos personales o de dispositivos sin necesidad y consentimiento.
6. **Comunicación embebida por defecto:** los módulos se integran mediante llamadas internas, sin abrir puertos. Cualquier necesidad de red debe justificarse y documentarse antes de implementarse.

---

## 2. Equipo de agentes ANC Team

La gobernanza propuesta comprende siete roles. Los nombres de productos o agentes externos describen funciones previstas y no significan que ya exista una integración activa.

| N.º | Agente/rol | Responsabilidad propuesta | Módulos previstos |
|---|---|---|---|
| 01 | **Claude — orquestador principal** | Planificar, dividir tareas, enrutar trabajo y sintetizar resultados. | `orquestador/`, `comite_agentes/orquestador.py` |
| 02 | **Grok Bot — vigía** | Supervisar servicios autorizados, detectar fallos y generar avisos. No rastrear personas. | `comite_agentes/vigia.py`, `observabilidad/` |
| 03 | **Hermes — agente local** | Inferencia sin conexión y procesamiento local cuando el dispositivo lo permita. | `ia_locales/`, `comite_agentes/ia_local.py` |
| 04 | **Antigravity — constructor** | Proponer y realizar cambios de código sujetos a revisión y pruebas. | `comite_agentes/constructor.py`, `estudios/` |
| 05 | **Dots — integraciones** | Conectar APIs y herramientas autorizadas; custodiar credenciales de forma segura. | `integraciones/`, `web/`, `ia_locales/herramientas/` |
| 06 | **OpenClaw — auditor/refutador** | Cuestionar resultados, detectar errores, riesgos y afirmaciones no verificadas. | `comite_agentes/regulador.py`, `verificacion/` |
| 07 | **AINEK Neural Computer — núcleo** | Mantener configuración y estado compartido, y coordinar servicios. | `configuracion.py`, `memoria/`, `utilidades/iniciar_motor.py` |

---

## 3. Capas del ecosistema e infraestructura de IA

Las siguientes capas son una guía de diseño; cada tecnología debe evaluarse por compatibilidad, privacidad, licencia y recursos disponibles antes de adoptarse.

| Capa | Referentes | Ubicación prevista |
|---|---|---|
| Modelos fundacionales | GPT, Claude, Gemini, Llama | `integraciones/proveedores_ia.py`, `ia_locales/modelos/` |
| Inferencia | Ollama, Hugging Face, Vertex AI | `ia_locales/`, `google_cloud/` |
| Agentes y orquestación | Agents SDK, LangGraph, LlamaIndex, CrewAI | `orquestador/`, `comite_agentes/` |
| Recuperación documental (RAG) | Haystack, RAGFlow, GraphRAG | `biblioteca/buscador_local.py`, `comite_agentes/buscador_documentos.py` |
| Embeddings | Proveedores locales o remotos | `ia_locales/embeddings/` |
| Herramientas e interoperabilidad | MCP SDK, FastMCP | `ia_locales/herramientas/`, `web/conectores/` |
| Seguridad y guardrails | Políticas de entrada/salida, listas permitidas | `seguridad/`, `terminal/lista_permitidos.py` |
| Observabilidad | Trazas, métricas y registros | `observabilidad/`, `utilidades/verificar_salud.py` |
| Memoria | Persistencia local con retención controlada | `memoria/` |
| Automatización | Tareas programadas con autorización | `orquestador/`, `actualizador.py` |
| Índices de conocimiento | Almacenamiento local indexado | `biblioteca/cache_conocimiento/` |

---

## 4. Catálogo funcional de herramientas de IA

Esta lista clasifica opciones por uso; no implica que el sistema las integre, recomiende o ejecute automáticamente.

- **Asistentes generales:** ChatGPT, Gemini, Claude, Grok, DeepSeek, Microsoft Copilot, Meta AI.
- **Búsqueda e investigación:** Perplexity, NotebookLM.
- **Programación y desarrollo:** GitHub Copilot, Cursor, Replit, Windsurf.
- **Imagen y diseño:** Midjourney, Adobe Firefly, Canva AI, Leonardo AI.
- **Video:** Sora, Google Veo, Runway, Kling AI.
- **Audio y voz:** ElevenLabs, Suno.
- **Productividad y contenido:** Notion AI, Gamma.

La selección de cualquier proveedor debe considerar disponibilidad, costo, términos de uso, tratamiento de datos, permisos y posibilidad de operar localmente.

---

## 5. Arquitectura de directorios y módulos

El árbol siguiente representa la arquitectura objetivo. Algunos directorios ya existen en el repositorio y otros son propuestas pendientes. La implementación debe avanzar por etapas, sin presentar módulos planeados como si ya estuvieran disponibles.

```text
Definitivo/
├── configuracion.py                  # Rutas y ajustes globales
├── orquestador/                      # Enrutamiento y flujo de tareas
│   ├── chatbot/                      # Interacción e historial
│   ├── asistente/                    # Perfil y preferencias
│   ├── catorce_funciones/            # Pipeline modular propuesto
│   ├── creacion_multimedia/          # Flujos multimedia propuestos
│   ├── nix_droid/                    # Propuestas de paquetes y estado
│   ├── librerias/                    # Utilidades internas
│   └── configuracion_orquestador.py  # Límites y reglas de enrutamiento
├── ia_locales/                       # Inferencia y recursos locales
│   ├── modelos/                      # Modelos; no incluir pesos sin licencia
│   ├── embeddings/                    # Vectorización
│   ├── herramientas/                  # Herramientas locales autorizadas
│   ├── librerias/                     # Adaptadores de inferencia
│   └── configuracion_ia_local.py     # Recursos y rutas
├── comite_agentes/                   # Coordinación y supervisión
│   ├── orquestador.py                # Planificación
│   ├── ia_local.py                   # Enlace con inferencia local
│   ├── buscador_documentos.py        # Recuperación documental
│   ├── regulador.py                  # Revisión crítica
│   ├── constructor.py                # Cambios sujetos a aprobación
│   ├── vigia.py                      # Supervisión de servicios autorizados
│   ├── notificador.py                # Avisos
│   └── estado.py                     # Estado del comité
├── verificacion/                     # Pruebas y revisión de cambios
│   ├── pruebas_automaticas.py
│   ├── validador_cambios.py
│   └── estado.py
├── seguridad/                        # Autorización, políticas y permisos
│   ├── lista_permitidos.py
│   ├── autorizacion.py
│   └── estado.py
├── observabilidad/                   # Registros y métricas
│   ├── registro_actividad.py
│   ├── metricas.py
│   └── estado.py
├── audio_voz/                        # Funciones de voz
│   ├── grabar_voz.py
│   ├── transcribir_a_texto.py
│   ├── texto_a_voz.py
│   └── estado.py
├── web/                              # Conectividad externa documentada
│   ├── buscador.py
│   ├── descargador.py
│   └── conectores/
├── terminal/                         # Ejecución limitada y auditable
│   ├── ejecutor.py
│   ├── lista_permitidos.py
│   ├── supervisor.py
│   └── estado.py
├── memoria/                          # Persistencia local y preferencias
│   ├── memoria_persistente.py
│   ├── preferencias_usuario.py
│   └── estado.py
├── acceso_root/                      # Solo si se justifica y autoriza
│   ├── shizuku/
│   ├── shell_root/
│   └── configuracion_acceso.py
├── google_cloud/                     # Adaptadores opcionales de nube
│   ├── consola_admin.py
│   ├── cloud_shell_puente.py
│   └── estado.py
├── estudios/                         # Herramientas de desarrollo
├── taller/                           # Diagnóstico y reparación autorizados
├── integraciones/                    # Proveedores y gestión de credenciales
│   ├── gestor_env.py
│   ├── vinculacion_google.py
│   ├── vinculacion_github.py
│   ├── proveedores_ia.py
│   └── estado.py
├── permisos/                         # Permisos del sistema operativo
├── biblioteca/                       # Conocimiento y búsqueda local
│   ├── cache_conocimiento/
│   │   ├── programacion_y_dev/
│   │   └── mi_zona/
│   ├── buscador_local.py
│   └── estado.py
├── herramientas/                     # Helpers de catálogo y diagnóstico existentes
│   ├── catalogo/
│   ├── casos/
│   ├── android/
│   └── usb/
├── utilidades/                       # Arranque, salud y mantenimiento
│   ├── iniciar_motor.py
│   ├── verificar_salud.py
│   └── limpiar_temporales.py
├── run_tests.py
└── test_all.py
```

### Módulos existentes relevantes

El repositorio ya contiene `configuracion.py`, `audio_voz/`, `comite_agentes/`, `herramientas/`, `ia_locales/`, `observabilidad/`, `orquestador/`, `seguridad/` y `verificacion/`, además de `run_tests.py` y `test_all.py`. El subsistema `herramientas/` proporciona un catálogo local, búsqueda, registro local de casos, planes de comprobaciones de solo lectura y validación de muestras de medición externas. Sus helpers no controlan hardware ni realizan flasheos.

---

## 6. Flujo de ejecución, auditoría y seguridad

Toda solicitud debe seguir un flujo verificable; una etapa puede detener el proceso si faltan permisos, datos o evidencia.

1. **Recepción e intención:** identificar la solicitud y aplicar preferencias sin recopilar información innecesaria.
2. **Búsqueda local:** consultar primero el conocimiento local y señalar su fecha o posible falta de vigencia.
3. **Planificación:** proponer pasos, dependencias, riesgos y si se requiere red, permisos elevados o confirmación.
4. **Construcción o acción:** limitarse a las capacidades permitidas; separar claramente lectura de modificación.
5. **Refutación y revisión:** buscar efectos secundarios, errores, filtración de credenciales y afirmaciones sin respaldo.
6. **Verificación:** ejecutar pruebas apropiadas y revisar cambios. No declarar éxito si no se verificó.
7. **Entrega y registro:** comunicar qué se hizo, qué no se hizo y qué requiere aprobación. Registrar solo lo necesario y con retención controlada.

### Reglas de seguridad

- Las acciones que modifican dispositivos, archivos, permisos o paquetes requieren confirmación explícita y específica.
- Las operaciones privilegiadas deben estar deshabilitadas por defecto, acotadas al dispositivo autorizado y sujetas a revisión; no se deben eludir bloqueos, controles de administración o protecciones antirrobo.
- No ejecutar comandos arbitrarios recibidos de modelos. Usar operaciones limitadas, validación de argumentos y registro de actividad.
- No guardar claves, tokens ni credenciales en el repositorio, registros o datos de casos. Usar almacenamiento de secretos apropiado al entorno.
- Las descargas deben ser solicitadas y visibles, provenir de fuentes verificables y comprobar integridad cuando corresponda.
- Las pruebas no sustituyen autorización ni revisión humana para acciones críticas.

---

## 7. Datos locales y monitoreo regional (Mi Zona)

**Ubicación propuesta:** `biblioteca/cache_conocimiento/mi_zona/`  
**Actualización:** trimestral o a petición del usuario, verificando la fecha, la fuente y la vigencia de cada dato.

Módulos de información pública previstos:

- `gobierno_y_tramites.py`: dependencias y trámites con enlaces oficiales.
- `mapas_y_ubicaciones.py`: referencias geográficas y ubicaciones públicas.
- `redes_y_paginas_oficiales.py`: directorio de canales oficiales.
- `noticias_y_avisos.py`: avisos públicos y fuentes verificables.
- `zonas_monitoreadas.py`: áreas geográficas configuradas por el usuario para consultar información pública.
- `alertas_sanitarias.py`: campañas, avisos epidemiológicos y salud pública usando fuentes oficiales.
- `actualizador.py`: actualización explícita o programada con registro de fuente y fecha.

El monitoreo regional debe limitarse a información pública y agregada, como avisos municipales, clima, servicios y salud pública. **No se crearán listas para seguir personas, familias o apellidos, ni perfiles, alertas o inferencias sobre individuos privados.** Las ubicaciones personales, contactos y datos sensibles no se incorporarán al catálogo o repositorio. Los datos locales deben tener propósito definido, retención mínima y una forma de borrado.

---

## 8. Protocolos de ejecución y gestión de paquetes (Nix-on-Droid)

**Ubicación propuesta:** `orquestador/nix_droid/gestor_paquetes.py`.

El gestor debe operar como un flujo de propuesta y confirmación, no como instalador autónomo:

1. Validar que el nombre del paquete proviene de una fuente de paquetes configurada y mostrar el motivo.
2. Informar al usuario sobre cambios, dependencias, tamaño aproximado y requisitos de red cuando se conozcan.
3. Esperar una confirmación explícita, asociada a esa propuesta concreta.
4. Ejecutar solo la operación aprobada; si el entorno no puede confirmar qué se ejecutará, cancelar.
5. Registrar resultado y error sin incluir secretos.

Estado mínimo sugerido:

```json
{
  "propuesta_valida": true,
  "paquete": "nombre-validado",
  "motivo": "explicación para el usuario",
  "confirmado": false,
  "estado": "pendiente_confirmacion"
}
```

La función de instalación debe rechazar por defecto cualquier llamada sin una autorización vigente y explícita. La integración con Nix-on-Droid debe implementarse y probarse en su entorno real; este documento no afirma que ya exista.

---

## 9. Estado actual y criterios de implementación

Este documento reúne la arquitectura objetivo en una sola especificación. Antes de implementar cada componente, se debe:

- comprobar qué código ya existe y evitar duplicarlo o reemplazarlo sin autorización;
- marcar cada función como **implementada**, **parcial** o **pendiente**, con evidencia en código y pruebas;
- mantener nombres de archivos y comentarios en español según las reglas del proyecto;
- compilar cada archivo Python nuevo o editado y ejecutar las pruebas pertinentes;
- documentar explícitamente cualquier acceso a red, dependencia, permiso del sistema o cambio persistente;
- revisar privacidad y seguridad, especialmente en registros, fotos, dispositivos y credenciales;
- no incluir firmware, claves, datos personales ni archivos privados en Git.

La prioridad es una base funcional, comprobable y segura, no completar el árbol por apariencia. La arquitectura se considera implementada únicamente cuando el código, las pruebas y la documentación coinciden.
