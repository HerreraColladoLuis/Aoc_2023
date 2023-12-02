# 12 red cubes, 13 green cubes, and 14 blue cubes

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
RED = 'red'
GREEN = 'green'
BLUE = 'blue'


def solve_p1():
    input_file = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-two.txt")
    total = 0
    for line in input_file.readlines():
        line = line.rstrip()
        juego = line.split(':')[0].split(' ')[1]
        excedido = False
        for set in line.split(':')[1].split(';'):
            if excedido:
                break
            for subset in set.split(','):
                if subset.split(' ')[2] == RED:
                    if int(subset.split(' ')[1]) > MAX_RED:
                        excedido = True
                        break
                elif subset.split(' ')[2] == GREEN:
                    if int(subset.split(' ')[1]) > MAX_GREEN:
                        excedido = True
                        break
                elif subset.split(' ')[2] == BLUE:
                    if int(subset.split(' ')[1]) > MAX_BLUE:
                        excedido = True
                        break
        if excedido:
            continue
        total = total + int(juego)
    print(total)


def solve_p2():
    input_file = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-two.txt")
    total = 0
    for line in input_file.readlines():
        min_red = 0
        min_blue = 0
        min_green = 0
        line = line.rstrip()
        for set in line.split(':')[1].split(';'):
            for subset in set.split(','):
                if subset.split(' ')[2] == RED:
                    if int(subset.split(' ')[1]) > min_red:
                        min_red = int(subset.split(' ')[1])
                elif subset.split(' ')[2] == GREEN:
                    if int(subset.split(' ')[1]) > min_green:
                        min_green = int(subset.split(' ')[1])
                elif subset.split(' ')[2] == BLUE:
                    if int(subset.split(' ')[1]) > min_blue:
                        min_blue = int(subset.split(' ')[1])
        subtotal = min_red*min_blue*min_green
        total = total + subtotal
    print(total)


solve_p2()
