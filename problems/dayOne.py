# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

import re

dicc_numeros = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
                "nine": "9"}


def solve_p1():
    input_file = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-one.txt")
    result = 0
    for line in input_file.readlines():
        parsed_line = re.sub("[a-z]", "", line).rstrip()
        n = int(parsed_line[0]) * 10 + int(parsed_line[len(parsed_line) - 1])
        result = result + n
    print(result)


def solve_p2():
    input_file = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-one.txt")
    result = 0
    i = 0
    for line in input_file.readlines():
        line = line.rstrip()
        new_line = ''
        for letra in line:
            new_line = new_line + letra
            for numero_escrito in dicc_numeros:
                if re.search(numero_escrito, new_line):
                    new_line = new_line.replace(numero_escrito, dicc_numeros[numero_escrito])
                    if letra == 't':
                        new_line = new_line + 't'
                    if letra == 'e':
                        new_line = new_line + 'e'
                    if letra == 'o':
                        new_line = new_line + 'o'
        print(new_line)
        parsed_line = re.sub("[a-z]", "", new_line).rstrip()
        n = int(parsed_line[0]) * 10 + int(parsed_line[len(parsed_line) - 1])
        result = result + n
    print(result)


solve_p2()
