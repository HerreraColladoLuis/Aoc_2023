# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

def dame_numeros(fila):
    numero = []
    numero.append('')
    numeros = []
    pos_letra = 0
    for letra in fila:
        if letra.isdigit():
            if numero[0] == '':
                numero.append(pos_letra)
            numero[0] += letra
        else:
            if numero[0] != '':
                numero.append(pos_letra-1)
                numeros.append(numero)
                numero = []
                numero.append('')
        pos_letra += 1
    if numero[0] != '':
        numero.append(pos_letra-1)
        numeros.append(numero)
    return numeros

def dame_simbolos(fila):
    simbolo = []
    simbolos = []
    pos_letra = 0
    for letra in fila:
        if is_symbol(letra):
            simbolo.append(letra)
            simbolo.append(pos_letra)
            simbolos.append(simbolo)
            simbolo = []
        pos_letra += 1
    return simbolos


def dame_asteriscos(fila):
    simbolo = []
    simbolos = []
    pos_letra = 0
    for letra in fila:
        if letra == '*':
            simbolo.append(letra)
            simbolo.append(pos_letra)
            simbolos.append(simbolo)
            simbolo = []
        pos_letra += 1
    return simbolos


def is_symbol(letra):
    return not letra.isdigit() and not letra.isalpha() and not letra == '.'


def comprobar_adyacente(numero, simbolos, fila):
    pos_inicial = numero[1]
    pos_final = numero[2]
    fila_superior = fila - 1
    fila_inferior = fila + 1
    for simbolo in simbolos[fila]:
        if simbolo[1] == pos_inicial-1 or simbolo[1] == pos_final+1:
            simbolo.append(numero[0])
            return True
    if fila_superior != -1:
        for simbolo in simbolos[fila_superior]:
            if simbolo[1] in range(pos_inicial-1,pos_final+2):
                simbolo.append(numero[0])
                return True
    if fila_inferior != len(simbolos):
        for simbolo in simbolos[fila_inferior]:
            if simbolo[1] in range(pos_inicial-1,pos_final+2):
                simbolo.append(numero[0])
                return True
    return False


def solve_p1():
    input_file = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-three.txt")
    numeros = []
    simbolos = []
    resultado = 0
    for linea in input_file.readlines():
        numeros.append(dame_numeros(linea.rstrip()))
        simbolos.append(dame_simbolos(linea.rstrip()))
    fila = 0
    for fila_numeros in numeros:
        for numero in fila_numeros:
            if comprobar_adyacente(numero, simbolos, fila):
                print(numero)
                resultado += int(numero[0])
        fila += 1
    print(resultado)


def solve_p2():
    input_file = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-three.txt")
    numeros = []
    simbolos = []
    resultado = 0
    for linea in input_file.readlines():
        numeros.append(dame_numeros(linea.rstrip()))
        simbolos.append(dame_asteriscos(linea.rstrip()))
    fila = 0
    print(numeros)
    print(simbolos)
    for fila_numeros in numeros:
        for numero in fila_numeros:
            if comprobar_adyacente(numero, simbolos, fila):
                print(numero)
        fila += 1
    print(simbolos)
    for fila_simbolos in simbolos:
        for simbolo in fila_simbolos:
            if len(simbolo) == 4:
                multi = int(simbolo[2]) * int(simbolo[3])
                resultado = resultado + multi
    print(resultado)


solve_p2()
