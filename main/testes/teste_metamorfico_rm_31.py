import unittest
from main.config.constantes import NomeRM
from main.config.entradas import Entradas

class TesteMetamorficoRM31(unittest.TestCase):

    def teste_basico(self):
        self.assertEqual(NomeRM.RM31,"2")


if __name__ == '__main__':
    unittest.main()