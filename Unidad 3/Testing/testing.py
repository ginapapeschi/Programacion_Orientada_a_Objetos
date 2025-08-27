import unittest
from claseCajadeAhorro import CajaDeAhorro

class TestCajaDeAhorro(unittest.TestCase):
    def setUp(self):
        self.__caja = CajaDeAhorro(1001, 35000, 0, 12345678, 'Castro', 'Luciana', '27-12345678-7')

    def test_depositos(self):
        self.__caja.depositar(5001)
        self.assertEqual(self.__caja.getSaldo(), 40001)

    def test_extracciones_OK(self):
        self.__caja.extraer(5001)
        self.__caja.extraer(31000)
        self.assertEqual(self.__caja.getSaldo(), 29999)

if __name__ == '__main__':
    unittest.main()