#0 3 6 9 12 15
#1 3 6 10 15 21
#10 13 16 21 30 45

#0   3   6   9  12  15 - 18
#  3   3   3   3   3 - 3
#    0   0   0   0 - 0

#10  13  16  21  30  45 - 68
#   3   3   5   9  15 - 23
#     0   2   4   6  - 8
#       2   2   2  - 2
#         0   0  - 0

# 0, 2, 6, 15, 45 --> 0, 2, 8, 23, 68

def calcula_siguiente(ultimos):
    siguientes = [0]
    for i in range(1, len(ultimos)):
        siguientes.append(ultimos[i] + siguientes[i-1])
    return siguientes[len(siguientes) - 1] + ultimos[0]


def siguiente(secuencia):
    ultimos = [secuencia[len(secuencia)-1]]
    while True:
        nueva_secuencia = []
        for i in range(0, len(secuencia) - 1):
            nueva_secuencia.append(secuencia[i+1] - secuencia[i])
        ultimos.append(nueva_secuencia[len(nueva_secuencia)-1])
        print(nueva_secuencia)
        if all(x == 0 for x in nueva_secuencia):
            print(ultimos)
            return calcula_siguiente(ultimos)
        secuencia = nueva_secuencia.copy()


def solve_p1():
    input_file = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-nine.txt")
    resultado = 0
    for linea in input_file.readlines():
        secuencia = [int(n) for n in linea.rstrip().split()]
        resultado = resultado + siguiente(secuencia)
        print(secuencia)
    print(resultado)

solve_p1()
