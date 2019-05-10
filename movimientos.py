import sys

def tablero_a_cadena(tablero):
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


def mover_torre(tablero, x_inicial, y_inicial, x_final, y_final):
    # Valido que se este moviendo una torre
    if tablero[y_inicial][x_inicial].lower() == 't':

        # Valido que se este moviendo en y
        if x_inicial == x_final and y_inicial != y_final:

            # Si me muevo hacia abajo
            if y_inicial < y_final:
                y_auxiliar = y_inicial + 1
            # Si no me muevo hacia abajo
            else:
                y_auxiliar = y_inicial - 1
            # Reviso  el camino por obstaculos
            for y in range(y_auxiliar, y_final):
                if tablero[y][x_inicial] != ' ':
                    raise Exception('No hay camino para mover la torre')

        # Valido el movimiento en x
        elif x_inicial != x_final and y_inicial == y_final:
            # validar si me muevo a la derecha
            if x_inicial < x_final:
                x_auxiliar = x_inicial + 1
            else:
                x_auxiliar = x_inicial - 1

            # Reviso el camino por obtaculos
            for x in range(x_auxiliar, x_final):
                if tablero[y_inicial][x] != ' ':
                    raise Exception('No hay camino para mover la torre')

        # El movimiento no es en linea recta o no hay movimiento
        else:
            raise Exception('Movimiento invalido para la torre')

        # Verifico la posición de destino
        if tablero[y_final][x_final] == ' ' \
                or (tablero[y_inicial][x_inicial].islower() != tablero[y_final][x_final].islower()):
            tablero[y_final][x_final] = tablero[y_inicial][x_inicial]
            tablero[y_inicial][x_inicial] = ' '
        else:
            raise Exception('No puedo comer mis propias piezas')

    else:
        raise Exception('La pieza en x = {0} y= {1} no es una torre'.format(x_inicial,y_inicial))
    return tablero