# CheessMoves
<center>![alt ajedrez](img/composicion-juegos-mesa_1284-18306.jpg)</center>

Su equipo ha sido comisionado para eleborar la funcionalidad de los movimientos de las
piezas del ajedrez en un tablero 8 x 8.

El tablero esta representado por una matriz de caracteres y las piezas estan representadas
de la siguiente forma (minusculas blancas y mayusculas negras):

- Peon `p`
- Torre `t`
- Caballo `k`
- Alfil `a`
- Reina `q`
- Rey `r`
- Vacio ` `

De esta manera un tablero inicial se puede representar de esta forma:

```python

tablero = [
['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']
]

```

Un estado en la partida se podría representar asi:

```python

tablero = [
['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
['p', 'p', 'p', ' ', 'p', 'p', 'p', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', 'p', ' ', ' ', ' ', 'p'],
['A', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['P', ' ', 'P', 'P', 'P', 'P', 'P', 'P'],
['T', 'K', ' ', 'R', 'Q', 'A', 'K', 'T']
]

```



------
## Instrucciones

1. Conforme un equipo de trabajo de 2 integrantes
1. Marque con estrella este repositorio
1. Realice un fork al repositorio
1. Revise la metodologia para sincronizar un fork con el original disponible 
<a href="https://help.github.com/en/articles/merging-an-upstream-repository-into-your-fork">en este enlace</a>
1. Uno de los integrantes creará las pruebras correspondientes a la función en una rama
1. El otro integrante desarrollará la funcionalidad asociada en otra rama
1. Se deben unir las ramas a mastes a través de Pull Request una vez esten listas
1. Siga las instrucciones del docente 
