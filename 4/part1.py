#!/bin/python3
result = 0
for card in [line.split()[2:] for line in open('data.txt', 'r').readlines()]:
    points = 0
    winningNums = []
    leftOrRight = True
    for part in card:
        if part == '|':
            leftOrRight = False
            continue
        if leftOrRight:
            winningNums.append(part)
        elif part in winningNums:
            if points == 0:
                points = 1
            else:
                points *= 2
    result += points
print(result)
