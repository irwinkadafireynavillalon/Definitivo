# Skills: catálogo y enrutamiento

Este directorio contiene instrucciones reutilizables para tareas específicas. Las skills están separadas de `orquestador/` y de `ia_locales/modelos/`; no incluyen pesos de modelos ni ejecutan acciones del sistema.

## Primera skill preparada

`activas/documentos/lectura_txt/` prepara contenido de texto para un modelo compatible. El catálogo la marca como activa para pruebas del flujo, pero la conexión real de inferencia queda pendiente: `ia_locales/configuracion_ia_local.py` solo declara rutas y `comite_agentes/ia_local.py` todavía no carga un modelo.

El cargador acepta una función de inferencia como adaptador. Si no se proporciona, devuelve `pendiente_conector_inferencia` y no simula una respuesta de modelo. La interfaz futura puede conectar ese adaptador sin cambiar el formato de las skills.

## Fuente de verdad y seguridad

- `catalogo/indice.json` es la fuente de verdad de nombres, categoría, estado y ruta de las skills.
- `catalogo/compatibilidades.json` declara el módulo y el modelo objetivo, junto con el estado verificado de la conexión.
- Solo se cargan skills con estado `activa_preparada`; las reservadas nunca se cargan automáticamente.
- Las skills son instrucciones, no permisos. No ejecutan comandos, instalan paquetes ni modifican archivos.
- No se descargan paquetes o modelos al iniciar la aplicación. La instalación requeriría un flujo separado, visible y confirmado.
- Ejecuta las pruebas desde la raíz con `python3 -m unittest skills.pruebas -v`.

La protección contra borrado o modificación no puede garantizarse desde estos archivos; requiere controles de permisos del sistema o reglas de protección de rama en GitHub.
