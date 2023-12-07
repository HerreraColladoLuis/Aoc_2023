#32T3K 765
#T55J5 684
#KK677 28
#KTJJT 220
#QQQJA 483

from functools import cmp_to_key


def dame_rango(mano: str):
    conteo_cartas = {}
    for carta in mano:
        if carta in conteo_cartas:
            conteo_cartas[carta] += 1
        else:
            conteo_cartas[carta] = 1
    conteo_cartas = dict(sorted(conteo_cartas.items(), key=lambda x: x[1], reverse=True))
    print(conteo_cartas)
    repetidas = list(conteo_cartas.values())[0]
    if repetidas == 1:
        return 1 #carta alta
    elif repetidas == 2 and len(conteo_cartas) == 4:
        return 2 #pareja
    elif repetidas == 2 and len(conteo_cartas) == 3:
        return 3 #doble pareja
    elif repetidas == 3 and len(conteo_cartas) == 3:
        return 4 #trio
    elif repetidas == 3 and len(conteo_cartas) == 2:
        return 5 #full house
    elif repetidas == 4:
        return 6 #4 of a kind
    elif repetidas == 5:
        return 7 #5 of a kind


def dame_valor_carta(carta: str):
    if carta == 'A':
        return 14
    elif carta == 'K':
        return 13
    elif carta == 'Q':
        return 12
    elif carta == 'J':
        return 11
    elif carta == 'T':
        return 10
    else:
        return int(carta)


def compara_cartas(mano1: str, mano2: str):
    for i in range(0, len(mano1)):
        valor1 = dame_valor_carta(mano1[i])
        valor2 = dame_valor_carta(mano2[i])
        if valor1 < valor2:
            return -1
        elif valor1 > valor2:
            return 1
    return 0


def comparar_manos(mano1: str, mano2: str):
    rango_mano1 = dame_rango(mano1)
    rango_mano2 = dame_rango(mano2)
    if rango_mano1 < rango_mano2:
        return -1
    elif rango_mano1 > rango_mano2:
        return 1
    else:
        return compara_cartas(mano1, mano2)


def solve_p1():
    input_file = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-seven.txt")
    manos = {}
    for linea in input_file.readlines():
        mano, valor = linea.rstrip().split()
        manos[mano] = int(valor)
    claves_ordenadas = sorted(manos, key=cmp_to_key(comparar_manos))
    manos_ordenadas = {clave: manos[clave] for clave in claves_ordenadas}
    print(manos_ordenadas)
    resultado = 0
    i = 0
    for valor in manos_ordenadas.values():
        i += 1
        resultado += valor * i
    print(resultado)


def solve_p1_aux():
    input_file = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-seven.txt")
    manos = {}
    for linea in input_file.readlines():
        mano, valor = linea.rstrip().split()
        manos[mano] = int(valor)
    for m in manos.keys():
        print(dame_rango(m))


solve_p1_aux()
#solve_p1()
