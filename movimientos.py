def tablero_a_cadena(tablero):
    """
    list of list -> str

    >>> tablero_a_cadena([['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'], ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']])
"['t', 'k', 'a', 'q', 'r', 'a', 'k', 't']\n['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']\n[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']\n[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']\n[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']\n[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']\n['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']\n['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']\n"
    >>> tablero_a_cadena(['', 'T', 'a'])


    :param tablero: list of list que representa el tablero
    :return: str que representa los valores del tablero
    """
    cadena = ""
    for fila in tablero:
        cadena += str(fila) + "\n"
    return cadena


def obtener_nombre_pieza(simbolo):
    """
    (str) -> str

    >>> obtener_nombre_pieza('p')
    'Peon blanco'
    >>> obtener_nombre_pieza('R')
    'Rey Negro'

    Retorna el nombre de la pieza del ajedrez dado su simbolo

    :param simbolo: la representacion de la pieza segun el enunciado
    :return: El nombre y color de la pieza
    """
    pass