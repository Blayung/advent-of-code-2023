#!/bin/python3
games = []
for line in open('data.txt', 'r').readlines():
    game = []
    for i in line.replace(':', ',').replace(';', ',').split(',')[1:]:
        part = i.split(' ')[1:]
        game.append((part[1].rstrip('\n'), int(part[0])))
    games.append(game)

result1 = 0
result2 = 0

for game_id, cubes in enumerate(games, 1):
    red_max = 0
    green_max = 0
    blue_max = 0

    checkIfItsEnough = True

    for cube in cubes:
        if cube[0] == 'red' and cube[1] > red_max:
            red_max = cube[1]
        if cube[0] == 'green' and cube[1] > green_max:
            green_max = cube[1]
        if cube[0] == 'blue' and cube[1] > blue_max:
            blue_max = cube[1]

        if checkIfItsEnough:
            if (cube[0] == 'red' and cube[1] > 12) or (cube[0] == 'green' and cube[1] > 13) or (cube[0] == 'blue' and cube[1] > 14):
                result1 += game_id
                checkIfItsEnough = False

    result2 += red_max * green_max * blue_max

print(f'{result1}\n{result2}')
