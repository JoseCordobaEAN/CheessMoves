def tablero_a_cadena(tablero):
    """
    list of list -> str

    >>> tablero_a_cadena([['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'], ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']])
    "['t', 'k', 'a', 'q', 'r', 'a', 'k', 't']
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']"

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
    tipo = 'Negro'
    if simbolo.islower():
        tipo = 'blanco'
    retorno = simbolo.lower()
    if retorno == 'p':
        return 'Peon '+tipo
    elif retorno == 't':
        return 'Torre ' + tipo
    elif retorno == 'k':
        return 'Caballo ' + tipo
    elif retorno == 'a':
        return 'Alfil ' + tipo
    elif retorno == 'q':
        return 'Reina ' + tipo
    elif retorno == 'r':
        return 'Rey ' + tipo
    else:
        return 'No es una pieza'