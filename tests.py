from unittest import TestCase
from movimientos import *

class Test_movimientos(TestCase):

    def test_tablero_a_cadena(self):
        dado = []
        espero = ""
        obtengo = tablero_a_cadena(dado)
        self.assertEquals(espero, obtengo)

    def test_obtener_nombre_pieza(self):
        dado = []
        espero = ""
        obtengo = obtener_nombre_pieza(dado)
        self.assertEquals(espero, obtengo)

    def test_mover_torre(self):
        dado = []
        espero = []
        obtengo = mover_torre(dado[0], dado[1], dado[2] , dado[3], dado[4])
        self.assertEquals(espero, obtengo)