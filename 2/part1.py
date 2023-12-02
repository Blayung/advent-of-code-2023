#!/bin/python3
games = []
for line in open('data.txt', 'r').readlines():
    game = []
    for i in line.replace(':', ',').replace(';', ',').split(',')[1:]:
        part = i.split(' ')[1:]
        game.append((part[1].rstrip('\n'), int(part[0])))
    games.append(game)

result = 0
for game_id, game in enumerate(games, 1):
    for cube in game:
        if (cube[0] == 'red' and cube[1] > 12) or (cube[0] == 'green' and cube[1] > 13) or (cube[0] == 'blue' and cube[1] > 14):
            break
    else:
        result += game_id

print(result)
