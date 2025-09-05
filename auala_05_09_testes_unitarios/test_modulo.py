# test_modulo.py

import modulo
import unittest

# Para criar uma suíte de testes, criamos uma classe que herda de `unittest.TestCase`.
# Esta classe nos dá acesso a vários métodos de asserção (self.assertEqual, etc.).
class TesteFatorial(unittest.TestCase):

    # O `self` é a instância da classe de teste, usado para acessar os métodos de asserção.
    
    def test_numeros_maiores_que_1(self):
        """Testa a função fatorial para números positivos maiores que 1."""
        # self.assertEqual(A, B) verifica se A é exatamente igual a B.
        self.assertEqual(modulo.fatorial(2), 2, "Fatorial de 2 deveria ser 2")
        self.assertEqual(modulo.fatorial(3), 6, "Fatorial de 3 deveria ser 6")
        self.assertEqual(modulo.fatorial(5), 120, "Fatorial de 5 deveria ser 120")

    def test_casos_base(self):
        """Testa os casos de fronteira (boundary values): 0 e 1."""
        self.assertEqual(modulo.fatorial(1), 1, "Fatorial de 1 deveria ser 1")
        self.assertEqual(modulo.fatorial(0), 1, "Fatorial de 0 deveria ser 1")

    def test_entradas_invalidas(self):
        """Testa se a função levanta os erros corretos para entradas inválidas."""
        # self.assertRaises(TipoDeErro, funcao, argumento1, ...)
        # Este teste passa se `modulo.fatorial("Oi")` levantar um TypeError.
        with self.assertRaises(TypeError, msg="Deveria levantar TypeError para strings"):
            modulo.fatorial("Oi")
            
        with self.assertRaises(TypeError, msg="Deveria levantar TypeError para floats"):
            modulo.fatorial(2.5)

        # Testa se a função levanta um ValueError para números negativos.
        with self.assertRaises(ValueError, msg="Deveria levantar ValueError para negativos"):
            modulo.fatorial(-5)

    def test_comparacao_de_floats(self):
        """Demonstra o uso de assertAlmostEqual para números de ponto flutuante."""
        # Nunca use assertEqual para comparar floats devido a imprecisões de hardware.
        num_1 = 2.00000001
        num_2 = 2.00000002
        # Verifica se os números são iguais até a 7ª casa decimal (neste caso, são).
        self.assertAlmostEqual(num_1, num_2, places=7)


# Este bloco é o "Executor de Testes".
# Quando você roda `python test_modulo.py`, o unittest descobre e executa
# todos os métodos que começam com "test_" dentro das classes de teste.
if __name__ == "__main__":
    unittest.main(verbosity=2)
