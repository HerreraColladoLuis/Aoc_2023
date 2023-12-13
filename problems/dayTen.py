# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

#7-F7-
#.FJ|7
#SJLL7
#|F--J
#LJ.LJ

P = {'|': (-1, 0, 1, 0),
     '-': (0, -1, 0, 1),
     'L': (-1, 0, 0, 1),
     'J': (-1, 0, 0, -1),
     '7': (1, 0, 0, -1),
     'F': (1, 0, 0, 1)} # TUBERÍAS
S = [] # INICIO Y FIN
T = [] # MAPA
CT = [] # COPIA DEL MAPA
MOVEMENTS = []


def mover(actual, anterior):
    fa = anterior[0]
    ca = anterior[1]
    ant = T[fa][ca]
    f = actual[0]
    c = actual[1]
    act = T[f][c]
    posibles = P[T[f][c]]
    if f + posibles[0] == fa and c + posibles[1] == ca:
        siguiente = [f + posibles[2], c + posibles[3]]
    else:
        siguiente = [f + posibles[0], c + posibles[1]]
    return [siguiente, actual]


def salir():
    f = S[0]
    c = S[1]
    siguientes = []
    if T[f-1][c] == '|' or T[f-1][c] == '7' or T[f-1][c] == 'F':
        siguientes.append([f-1, c])
    if T[f][c+1] == '-' or T[f][c+1] == 'J' or T[f][c+1] == '7':
        siguientes.append([f, c+1])
    if T[f+1][c] == '|' or T[f+1][c] == 'L' or T[f+1][c] == 'J':
        siguientes.append([f+1, c])
    if T[f][c-1] == '-' or T[f][c-1] == 'L' or T[f][c-1] == 'F':
        siguientes.append([f, c-1])
    return siguientes


def solve_p1():
    input_file = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-ten.txt")
    i = 0
    for linea in input_file.readlines():
        p = linea.find('S')
        if p != -1:
            S.append(i)
            S.append(p)
        T.append(linea.rstrip())
        i = i+1
    print(T)
    print(S)
    actual, actual_1 = [a for a in salir()]
    anterior = S.copy()
    anterior_1 = S.copy()
    pasos = 1
    while True:
        actual, anterior = [b for b in mover(actual, anterior)]
        actual_1, anterior_1 = [f for f in mover(actual_1, anterior_1)]
        pasos += 1
        if actual == actual_1:
            print(pasos)
            return pasos


solve_p1()
