#   ...#......
#   .......#..
#   #.........
#   ..........
#   ......#...
#   .#........
#   .........#
#   ..........
#   .......#..
#   #...#.....
import itertools

T = []  # Mapa principal
G = {}  # Galaxias
C = []  # Combinaciones de galaxias


def solve_p1():
    input_file = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-eleven.txt")
    for linea in input_file.readlines():
        T.append(linea.rstrip())
        if all(c == '.' for c in linea.rstrip()):
            T.append(linea.rstrip())
    ##############
    i = -1
    while True:
        i += 1
        if i > len(T[0]) - 1:
            break
        crear = True
        for j in range(0, len(T)):
            if '#' == T[j][i]:
                crear = False
                break
        if crear:
            for z in range(0, len(T)):
                T[z] = T[z][:i] + '.' + T[z][i:]
            i += 1
    ##############
    i = 1
    for a in range(0, len(T)):
        print(T[a])
        for j in range(0, len(T[a])):
            if '#' == T[a][j]:
                G[i] = [a, j]
                i += 1
    lista_galaxias = list(G.items())
    C = itertools.combinations(lista_galaxias, 2)
    print(lista_galaxias)
    resultado = 0
    for c in C:
        print(c)
        par1 = c[0]
        par2 = c[1]
        dif_fila = par2[1][0] - par1[1][0]
        dif_columna = par2[1][1] - par1[1][1]
        path = abs(dif_fila) + abs(dif_columna)
        resultado += path
        print(path)
    print(resultado)


solve_p1()
