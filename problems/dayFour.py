#Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
#Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
#Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
#Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
#Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
#Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

#1 = 1
#2 = 2
#3 = 4
#4 = 8
#5 = 16
#6 = 32
#7 = 64

def solve_p1():
    input_file = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-four.txt")
    resultado = 0
    for line in input_file.readlines():
        line = line.rstrip()
        ganadores = set(line.split(':')[1].split('|')[0].split())
        mios = set(line.split(':')[1].split('|')[1].split())
        coincidencias = ganadores & mios
        if len(coincidencias) > 0:
            resultado = resultado + 2**(len(coincidencias)-1)
        print(coincidencias)
    print(resultado)


def solve_p2():
    input_file_1 = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-four.txt")
    input_file = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-four.txt")
    resultado = 0
    cards = []
    for indice in range(1, len(input_file_1.readlines())+1):
        cards.append([indice, 1])
    indice = 0
    for line in input_file.readlines():
        line = line.rstrip()
        ganadores = set(line.split(':')[1].split('|')[0].split())
        mios = set(line.split(':')[1].split('|')[1].split())
        coincidencias = ganadores & mios
        for c in range(0, cards[indice][1]):
            aux_indice = indice + 1
            for i in range(0, len(coincidencias)):
                cards[aux_indice][1] += 1
                aux_indice += 1
        indice += 1
        print(coincidencias)
    for card in cards:
        resultado = resultado + card[1]
    print(cards)
    print(resultado)


solve_p2()
