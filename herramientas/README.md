# Herramientas de diagnóstico y reparación

Esta carpeta integra de forma independiente y aditiva capacidades de referencia del proyecto fuente en `Definitivo`. Los nombres de carpetas, archivos, funciones y comentarios nuevos están en español. No se modificaron módulos existentes del proyecto.

## Contenido

- `catalogo/herramientas.json`: categorías universales y referencias para Android, Apple, PC, USB, UVC, Qualcomm EDL, MediaTek y medios de arranque.
- `busqueda.py`: búsqueda local de candidatos sin instalar ni ejecutar programas.
- `casos/registro.py`: registro JSONL local, referencias a fotos privadas y varios dispositivos por caso.
- `lotes_y_reportes.py`: planes no ejecutables de comprobaciones de solo lectura, avisos para la app y resúmenes agregados.
- `usb/medicion.py` y `usb/formato_medicion.json`: validación estructural de muestras de un adaptador externo.
- `android/administracion_aplicaciones.json`: contrato para inspeccionar y administrar aplicaciones Android con autorización del propietario.
- `pruebas.py`: pruebas locales sin hardware real.

## Uso local

Desde la raíz del proyecto:

```sh
python3 -m herramientas.busqueda --validar
python3 -m herramientas.busqueda --categoria telefonos --marca Samsung
python3 -m unittest herramientas.pruebas -v
```

La búsqueda solo devuelve información del catálogo; no controla hardware. La integración con cámara, notificaciones de Android, permisos USB, voz en segundo plano y ejecución real ADB/Fastboot requiere implementación en la aplicación destino, fuera de estos helpers Python.

## Seguridad y compatibilidad

Las referencias y funciones son candidatas, no una promesa de compatibilidad universal. VID/PID no confirma el modelo exacto; sin identidad suficiente, usar revisión manual. Los lotes solo admiten comprobaciones declaradas de lectura. No se incluyen scripts ejecutables de desbloqueo, flasheo, EDL, borrado de particiones ni bypass. Las referencias para reparación destructiva remiten a documentación oficial y requieren acción manual del técnico.

Las imágenes deben guardarse en almacenamiento privado local; el registro solo conserva una ruta relativa. Los casos no necesitan por defecto nombres, teléfonos, correo, IMEI, seriales, contraseñas ni tokens. No hay escaneo IP, puertos de red ni requisito de WEP. Las descargas de herramientas/firmware, si se implementan, deben ser visibles, oficiales, a petición y fuera del repositorio.

Los esquemáticos y boardviews solo se consultan si el usuario tiene derecho de acceso. La corriente de entrada sola no identifica un componente en corto; sin medidor calibrado no se inventan valores.

## Scripts de referencia

Los scripts de origen que desbloquean el gestor de arranque, escriben particiones, flashean firmware o afirman mediciones que no realizan **no se copian como ejecutables**. Se conserva su función como entradas de referencia y se deja el control de operaciones destructivas al técnico y al procedimiento oficial específico del modelo.
