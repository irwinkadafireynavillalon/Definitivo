"""Pruebas de catálogo, búsqueda, casos, mediciones y planes locales."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from herramientas.busqueda import (
    buscar_herramientas, cargar_catalogo, validar_catalogo,
)
from herramientas.casos.registro import (
    agregar_dispositivo, agregar_referencia_foto, crear_caso, guardar_caso,
)
from herramientas.lotes_y_reportes import crear_plan_lote
from herramientas.usb.medicion import estado_medicion, validar_medicion


class PruebasCatalogo(unittest.TestCase):
    def test_carga_catalogo_predeterminado_y_valida_ids(self) -> None:
        catalogo = cargar_catalogo()
        self.assertGreater(len(catalogo["herramientas"]), 0)
        self.assertEqual(validar_catalogo(catalogo), [])

    def test_busqueda_por_categoria_protocolo_y_modelo_no_confirmado(self) -> None:
        resultados = buscar_herramientas(
            cargar_catalogo(), categoria="telefonos", protocolo="fastboot", modelo="modelo-x"
        )
        self.assertTrue(resultados)
        self.assertTrue(all(x["compatibilidad_modelo"] == "no_confirmada" for x in resultados))

    def test_detecta_ids_duplicados(self) -> None:
        errores = validar_catalogo({"herramientas": [{"id": "x"}, {"id": "x"}]})
        self.assertEqual(len(errores), 1)


class PruebasCasosYLotes(unittest.TestCase):
    def test_caso_dispositivo_foto_y_guardado_privado(self) -> None:
        caso = crear_caso(categoria="telefonos")
        agregar_dispositivo(caso, etiqueta="equipo", transporte="usb_otg")
        agregar_referencia_foto(caso, "casos/demo/frente.jpg")
        with tempfile.TemporaryDirectory() as directorio:
            ruta = Path(directorio) / "casos.jsonl"
            guardar_caso(ruta, caso)
            self.assertIn('"id_caso"', ruta.read_text(encoding="utf-8"))

    def test_rechaza_ruta_de_foto_fuera_de_casos(self) -> None:
        with self.assertRaises(ValueError):
            agregar_referencia_foto(crear_caso(categoria="telefonos"), "../secreto.jpg")

    def test_plan_lote_no_inicia_ejecucion_y_rechaza_escritura(self) -> None:
        plan = crear_plan_lote([{"id_dispositivo": "1"}], ["inventario_usb"])
        self.assertFalse(plan["ejecucion_iniciada"])
        with self.assertRaises(ValueError):
            crear_plan_lote([{"id_dispositivo": "1"}], ["flashear"])


class PruebasMedicion(unittest.TestCase):
    def test_medicion_calibrada_solo_queda_lista_para_revision(self) -> None:
        datos = {"protocolo": "medicion-json-v1", "medicion": {
            "id_calibracion": "cal-1", "muestras": [
                {"tiempo_ns": 1, "voltaje_mv": 5000, "corriente_ma": 100},
                {"tiempo_ns": 2, "voltaje_mv": 5000, "corriente_ma": 110},
            ],
        }}
        self.assertEqual(validar_medicion(datos), (True, []))
        resultado = estado_medicion(datos)
        self.assertEqual(resultado["estado"], "lista_para_revision_tecnica")
        self.assertIsNone(resultado["diagnostico"])


if __name__ == "__main__":
    unittest.main()
