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

T = []   # Mapa principal
G = {}   # Galaxias
C = []   # Combinaciones de galaxias
CV = []  # Columnas vacías
FV = []  # Filas vacías


def solve_p1():
    input_file = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-eleven.txt")
    i = 0
    for linea in input_file.readlines():
        T.append(linea.rstrip())
        if all(c == '.' for c in linea.rstrip()):
            FV.append(i)
        i += 1
    ##############
    i = -1
    while True:
        i += 1
        if i > len(T[0]) - 1:
            break
        vacia = True
        for j in range(0, len(T)):
            if '#' == T[j][i]:
                vacia = False
                break
        if vacia:
            CV.append(i)
    ##############
    print(FV)
    print(CV)
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
        filas_en_medio = sum(par1[1][0] < n < par2[1][0] for n in FV) + sum(par2[1][0] < n < par1[1][0] for n in FV)
        columnas_en_medio = sum(par1[1][1] < n < par2[1][1] for n in CV) + sum(par2[1][1] < n < par1[1][1] for n in CV)
        filas_en_medio = filas_en_medio * 999999
        columnas_en_medio = columnas_en_medio * 999999
        #if filas_en_medio > 0 or columnas_en_medio > 0:
        #    total_filas_columnas_ += filas_en_medio + columnas_en_medio
        dif_fila = par2[1][0] - par1[1][0]
        dif_columna = par2[1][1] - par1[1][1]
        path = abs(dif_fila) + abs(dif_columna) + filas_en_medio + columnas_en_medio
        resultado += path
        print(path)
    print(len(FV) + len(CV))
    print(resultado)


solve_p1()
