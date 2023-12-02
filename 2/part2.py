#!/bin/python3
result = 0
for line in open('data.txt', 'r').readlines():
    game = []
    for i in line.replace(':', ',').replace(';', ',').split(',')[1:]:
        part = i.split(' ')[1:]
        game.append((part[1].rstrip('\n'), int(part[0])))

    red_max = 0
    green_max = 0
    blue_max = 0

    for cube in game:
        if cube[0] == 'red':
            if cube[1] > red_max:
                red_max = cube[1]
        elif cube[0] == 'green':
            if cube[1] > green_max:
                green_max = cube[1]
        elif cube[0] == 'blue':
            if cube[1] > blue_max:
                blue_max = cube[1]

    result += red_max * green_max * blue_max

print(result)
