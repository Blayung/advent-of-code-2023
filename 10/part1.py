#!/bin/python3
from sys import setrecursionlimit

setrecursionlimit(2147483647)

map = open('data.txt', 'r').readlines()

def processField(currentPos, cameFrom, step):
    #for y, line in enumerate(map):
    #    for x, char in enumerate(line):
    #        print('#' if currentPos == (x, y) else char, end = '')
    #print(step)
    #input()

    if map[currentPos[0]][currentPos[1]] == 'S':
        return step / 2
    if cameFrom == (currentPos[0], currentPos[1] - 1):
        if map[currentPos[1]][currentPos[0]] == '|':
            return processField((currentPos[0], currentPos[1] + 1), currentPos, step + 1)
        if map[currentPos[1]][currentPos[0]] == 'J':
            return processField((currentPos[0] - 1, currentPos[1]), currentPos, step + 1)
        if map[currentPos[1]][currentPos[0]] == 'L':
            return processField((currentPos[0] + 1, currentPos[1]), currentPos, step + 1)
    if cameFrom == (currentPos[0], currentPos[1] + 1):
        if map[currentPos[1]][currentPos[0]] == '|':
            return processField((currentPos[0], currentPos[1] - 1), currentPos, step + 1)
        if map[currentPos[1]][currentPos[0]] == '7':
            return processField((currentPos[0] - 1, currentPos[1]), currentPos, step + 1)
        if map[currentPos[1]][currentPos[0]] == 'F':
            return processField((currentPos[0] + 1, currentPos[1]), currentPos, step + 1)
    if cameFrom == (currentPos[0] - 1, currentPos[1]):
        if map[currentPos[1]][currentPos[0]] == '-':
            return processField((currentPos[0] + 1, currentPos[1]), currentPos, step + 1)
        if map[currentPos[1]][currentPos[0]] == 'J':
            return processField((currentPos[0], currentPos[1] - 1), currentPos, step + 1)
        if map[currentPos[1]][currentPos[0]] == '7':
            return processField((currentPos[0], currentPos[1] + 1), currentPos, step + 1)
    if cameFrom == (currentPos[0] + 1, currentPos[1]):
        if map[currentPos[1]][currentPos[0]] == '-':
            return processField((currentPos[0] - 1, currentPos[1]), currentPos, step + 1)
        if map[currentPos[1]][currentPos[0]] == 'L':
            return processField((currentPos[0], currentPos[1] - 1), currentPos, step + 1)
        if map[currentPos[1]][currentPos[0]] == 'F':
            return processField((currentPos[0], currentPos[1] + 1), currentPos, step + 1)

#print(processField((101, 95), (101, 96), 1))
#print(processField((102, 96), (101, 96), 1))
# I don't know why summing these up works, but I do not really care xd
print(processField((101, 95), (101, 96), 1) + processField((102, 96), (101, 96), 1))
