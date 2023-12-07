#seeds: 79 14 55 13

#seed-to-soil map:
#50 98 2
#52 50 48

#soil-to-fertilizer map:
#0 15 37
#37 52 2
#39 0 15

#fertilizer-to-water map:
#49 53 8
#0 11 42
#42 0 7
#57 7 4

#water-to-light map:
#88 18 7
#18 25 70

#light-to-temperature map:
#45 77 23
#81 45 19
#68 64 13

#temperature-to-humidity map:
#0 69 1
#1 0 69

#humidity-to-location map:
#60 56 37
#56 93 4

def obtener_mapeo(list, input_file):
    mapeos = []
    borrados = []
    while True:
        linea = input_file.readline().rstrip()
        if linea == '':
            break
        des_range = int(linea.split()[0])
        source_range = int(linea.split()[1])
        range_length = int(linea.split()[2])
        for dato in list:
            mapeo = None
            if dato in range(source_range, source_range + range_length):
                mapeo = des_range + (dato - source_range)
            if mapeo is not None:
                mapeos.append(mapeo)
                borrados.append(dato)
    for sobrante in list:
        if sobrante not in borrados:
            mapeos.append(sobrante)
    return mapeos


def obtener_semillas(list):
    seeds = []
    i = 0
    pair = []
    while i < len(list):
        pair.append(int(list[i]))
        pair.append(int(list[i+1]))
        for j in range(0, pair[1]):
            seeds.append(pair[0] + j)
        print('1 pair done')
        i = i + 2
    return seeds


def solve_p1():
    input_file = open("/Users/n343110/PyCharmProjects/Aoc_2023/inputs/input-day-five.txt")
    linea = input_file.readline().rstrip()
    if linea.split(':')[0] == 'seeds':
        seeds = obtener_semillas(linea.split(':')[1].split())

    while True:
        linea = input_file.readline()
        if not linea:
            break
        linea = linea.rstrip()
        if linea.split(':')[0] == 'seed-to-soil map':
            soils = obtener_mapeo(seeds, input_file)
        elif linea.split(':')[0] == 'soil-to-fertilizer map':
            fertilizers = obtener_mapeo(soils, input_file)
        elif linea.split(':')[0] == 'fertilizer-to-water map':
            waters = obtener_mapeo(fertilizers, input_file)
        elif linea.split(':')[0] == 'water-to-light map':
            lights = obtener_mapeo(waters, input_file)
        elif linea.split(':')[0] == 'light-to-temperature map':
            temperatures = obtener_mapeo(lights, input_file)
        elif linea.split(':')[0] == 'temperature-to-humidity map':
            humidities = obtener_mapeo(temperatures, input_file)
        elif linea.split(':')[0] == 'humidity-to-location map':
            locations = obtener_mapeo(humidities, input_file)
        else:
            continue
    print(min(locations))


solve_p1()
