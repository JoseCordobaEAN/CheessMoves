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

        #Prueba movimiento vertical
        dado = [[
['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']
],0, 7, 0, 2 ] # lista con los parametros a usar en la función
        espero = [
['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
[' ', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']
]

        # Prueba movimiento horizontal
        print("Dado\n",
              tablero_a_cadena(dado[0]), dado[1], dado[2] , dado[3], dado[4])
        print("espero\n",
              tablero_a_cadena(espero))
        obtengo = mover_torre(dado[0], dado[1], dado[2], dado[3], dado[4])
        print("obtengo\n",
              tablero_a_cadena(obtengo))
        self.assertEqual(espero, obtengo)

        dado = [[
            ['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['T', ' ', ' ', 'R', 'Q', 'A', 'K', 'T']
        ], 0, 7, 2, 7]  # lista con los parametros a usar en la función
        espero = [
            ['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            [' ', ' ', 'T', 'R', 'Q', 'A', 'K', 'T']
        ]

        print("Dado\n",
              tablero_a_cadena(dado[0]), dado[1], dado[2], dado[3], dado[4])
        print("espero\n",
              tablero_a_cadena(espero))
        obtengo = mover_torre(dado[0], dado[1], dado[2], dado[3], dado[4])
        print("obtengo\n",
              tablero_a_cadena(obtengo))
        self.assertEqual(espero, obtengo)

