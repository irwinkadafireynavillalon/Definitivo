"""Pruebas unitarias del catálogo y el flujo inicial de skills."""
import unittest

from skills.cargador_skills import ejecutar_skill, preparar_solicitud
from skills.catalogo.estado import listar_skills


class PruebasSkills(unittest.TestCase):
    def test_indice_lista_skill_inicial(self):
        skills = listar_skills(estado="activa_preparada")
        self.assertIn("lectura_txt", [skill.get("id") for skill in skills])

    def test_solicitud_indica_que_inferencia_sigue_pendiente(self):
        resultado = preparar_solicitud("lectura_txt", "Texto de prueba")
        self.assertEqual(resultado["estado"], "preparada_pendiente_de_inferencia")
        self.assertEqual(resultado["modelo_local"], "entender_texto")
        self.assertIn("Texto de prueba", resultado["solicitud"])

    def test_no_simula_respuesta_sin_adaptador(self):
        resultado = ejecutar_skill("lectura_txt", "Texto de prueba")
        self.assertNotIn("respuesta", resultado)
        self.assertEqual(resultado["estado"], "preparada_pendiente_de_inferencia")

    def test_adaptador_recibe_modelo_y_solicitud(self):
        llamadas = []

        def adaptador(modelo: str, solicitud: str) -> str:
            llamadas.append((modelo, solicitud))
            return "Respuesta de prueba"

        resultado = ejecutar_skill("lectura_txt", "Texto de prueba", adaptador)
        self.assertEqual(llamadas[0][0], "entender_texto")
        self.assertIn("Texto de prueba", llamadas[0][1])
        self.assertEqual(resultado["respuesta"], "Respuesta de prueba")
        self.assertEqual(resultado["estado"], "respuesta_recibida")

    def test_no_carga_skill_desconocida(self):
        with self.assertRaises(KeyError):
            preparar_solicitud("no_existe", "Texto")


if __name__ == "__main__":
    unittest.main()
