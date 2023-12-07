#Time:      7  15   30
#Distance:  9  40  200

def solve_p1():
    input_file = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-six.txt")
    tiempos = input_file.readline().rstrip().split(':')[1].split()
    distancias = input_file.readline().rstrip().split(':')[1].split()
    resultado = 1
    for i in range(0, len(tiempos)):
        veces_ganadoras = 0
        t = int(tiempos[i])
        d = int(distancias[i])
        for j in range(1, t):
            if ((t-j)*j) > d:
                veces_ganadoras += 1
        resultado = resultado * veces_ganadoras
    print(resultado)


def solve_p2():
    input_file = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-six.txt")
    t = int(''.join(map(str, input_file.readline().rstrip().split(':')[1].split())))
    d = int(''.join(map(str, input_file.readline().rstrip().split(':')[1].split())))
    veces_ganadoras = 0
    for j in range(1, t):
        if ((t - j) * j) > d:
            veces_ganadoras += 1
    print(veces_ganadoras)


solve_p2()
