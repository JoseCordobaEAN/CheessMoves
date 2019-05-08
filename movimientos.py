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
    
def mover_torre(tablero, x0,y0,x1,y1):
    if tablero[x0][y0] != 't' or tablero[x0][y0] != 'T':
        raise Exception("La pieza debe ser una torre")
    
    # movimiento horizontal o vertical
    movimiento_horizontal = false;
    if x0!=x1 and y0==y1:
        movimiento_horizontal = true;
    elif y0!=y1 and x0==x1:
        movimiento_horizontal = false;
    else:
        raise Exception("La pieza no se movio o se mueve de forma no recta.")
    
    # validar las recta
    if movimiento_horizontal:
        min_x = min(x0,x1)
        max_x = max(x0,x1)
        for x in range(min_x, max_x+1):
            if tablero[x][y0] != ' ':
                raise Exception("Hay un obstaculo en el camino")
    else:
        min_y = min(y0,y1)
        max_y = max(y0,y1)
        for y in range(min_y, max_y+1):
            if tablero[x0][y] != ' ':
                raise Exception("Hay un obstaculo en el camino")
    
    # mover pieza
    tablero[x1][y1] = tablero[x0][y0]
    tablero[x0][y0] = ' '
    
    # retorno el nuevo tablero    
    return tablero
    
