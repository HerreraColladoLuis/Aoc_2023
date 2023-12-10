#RL

#AAA = (BBB, CCC)
#BBB = (DDD, EEE)
#CCC = (ZZZ, GGG)
#DDD = (DDD, DDD)
#EEE = (EEE, EEE)
#GGG = (GGG, GGG)
#ZZZ = (ZZZ, ZZZ)

from math import gcd
from functools import reduce


def solve_p1():
    input_file = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-eight.txt")
    nodos = {}
    instrucciones = input_file.readline().rstrip()
    sig = input_file.readline().rstrip()
    while sig != '':
        instrucciones += sig
        sig = input_file.readline().rstrip()
    print(instrucciones)
    for linea in input_file.readlines():
        clave: str = linea.rstrip().split('=')[0].strip()
        valor: tuple = tuple(linea.rstrip().split('=')[1].strip()[1:-1].split(', '))
        nodos[clave] = valor
    print(nodos)
    pasos = 0
    actual = 'AAA'
    while True:
        for ins in instrucciones:
            if actual == 'ZZZ':
                print(pasos)
                return
            i = 0
            if ins == 'R':
                i = 1
            actual = nodos[actual][i]
            pasos += 1


def mover(nodos_actuales, nodos, ins):
    nodos_nuevos = []
    i = 0
    if ins == 'R':
        i = 1
    for actual in nodos_actuales:
        nodos_nuevos.append(nodos[actual][i])
    return nodos_nuevos


def mover_uno(actual, nodos, ins):
    i = 0
    if ins == 'R':
        i = 1
    return nodos[actual][i]


def son_todos_final(nodos_actuales):
    for n in nodos_actuales:
        if n[2] != 'Z':
            return False
    return True


def mcm_numeros(lista):
    """ Calcula el mínimo común múltiplo de una lista de números. """

    def mcm(a, b):
        return a * b // gcd(a, b)

    return reduce(mcm, lista)


def solve_p2():
    input_file = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-eight.txt")
    nodos = {}
    instrucciones = input_file.readline().rstrip()
    sig = input_file.readline().rstrip()
    while sig != '':
        instrucciones += sig
        sig = input_file.readline().rstrip()
    print(instrucciones)
    for linea in input_file.readlines():
        clave: str = linea.rstrip().split('=')[0].strip()
        valor: list = list(linea.rstrip().split('=')[1].strip()[1:-1].split(', '))
        nodos[clave] = valor
    print(nodos)
    nodos_actuales = [c for c in nodos.keys() if c[2] == 'A']
    lista_pasos = []
    print(nodos_actuales)
    for j in range(0, len(nodos_actuales)):
        encontrado = False
        actual = nodos_actuales[j]
        pasos = 0
        while True:
            for ins in instrucciones:
                if actual[2] == 'Z':
                    encontrado = True
                    print(pasos)
                    lista_pasos.append(pasos)
                    break
                actual = mover_uno(actual, nodos, ins)
                pasos += 1
            if encontrado:
                break
    print(mcm_numeros(lista_pasos))


solve_p2()
