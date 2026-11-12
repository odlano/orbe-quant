
import unittest

from classificador_ev import analisar_oportunidade
from gestao_risco import calcular_entrada
from orbe_quant import gerar_relatorio


class TesteOrbeQuant(unittest.TestCase):

    def test_odd_justa(self):
        resultado = analisar_oportunidade(0.70, 1.80)
        self.assertEqual(resultado["odd_justa"], 1.43)

    def test_ev_positivo(self):
        resultado = analisar_oportunidade(0.70, 1.80)
        self.assertGreater(resultado["valor_esperado"], 0)

    def test_ev_negativo(self):
        resultado = analisar_oportunidade(0.50, 1.50)
        self.assertEqual(
            resultado["classificacao"],
            "EV NEGATIVO"
        )

    def test_bloqueio_de_entrada(self):
        resultado = calcular_entrada(
            1000, 0.40, 1.50
        )
        self.assertEqual(resultado["entrada"], 0)

    def test_integrador(self):
        resultado = gerar_relatorio(
            {"Over 1.5": 80},
            {"Over 1.5": 1.70},
            1000
        )
        self.assertEqual(len(resultado), 1)


if __name__ == "__main__":
    unittest.main()
  
