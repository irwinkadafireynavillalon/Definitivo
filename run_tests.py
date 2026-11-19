"""Ejecutar pruebas rápidas de los módulos placeholder.
Importa cada archivo y llama a la función principal que exista.
Si alguna función lanza excepción o devuelve False, se considerará fallo.
"""
import sys, traceback

def check_func(module, func_name):
    try:
        func = getattr(module, func_name)
    except AttributeError:
        print(f"[ERROR] {module.__name__} no tiene la función {func_name}")
        return False
    try:
        result = func()
        if result is False:
            print(f"[FAIL] {module.__name__}.{func_name} devolvió False")
            return False
        print(f"[OK] {module.__name__}.{func_name} -> {result}")
        return True
    except Exception:
        print(f"[EXCEPTION] {module.__name__}.{func_name}")
        traceback.print_exc()
        return False

def main():
    success = True
    # verificacion
    import verificacion.pruebas_automaticas as pa
    success &= check_func(pa, 'ejecutar_pruebas')
    import verificacion.validador_cambios as vc
    success &= check_func(vc, 'validar_cambios')
    # seguridad
    import seguridad.lista_permitidos as lp
    # No hay función principal, solo la lista
    # seguridad.autorizacion
    import seguridad.autorizacion as auth
    if hasattr(auth, 'es_autorizado'):
        print('[INFO] seguridad.autorizacion.es_autorizado está presente')
    # observabilidad
    import observabilidad.registro_actividad as ra
    ra.registrar('prueba')
    # audio_voz
    import audio_voz.grabar_voz as gv
    gv.grabar()
    import audio_voz.transcribir_a_texto as tt
    tt.transcribir()
    import audio_voz.texto_a_voz as tv
    tv.sintetizar('hola')
    # orquestador/nix_droid
    import orquestador.nix_droid.gestor_paquetes as gp
    gp.proponer_instalacion('example')
    print('Todas las llamadas realizadas.')
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
