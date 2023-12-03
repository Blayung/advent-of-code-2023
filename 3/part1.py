#!/bin/python3
currentNum = ''
partNums = []
symbols = []

for y, line in enumerate(open('data.txt', 'r').readlines()):
    for x, char in enumerate(line):
        if char.isdigit():
            currentNum += char
        else:
            if len(currentNum) > 0:
                partNums.append((x, y, currentNum))
                currentNum = ''
            if char != '.' and char != '\n':
                symbols.append((x, y))

result = 0

for partNum in partNums:
    coordsToCheck = [
        (partNum[0], partNum[1]),
        (partNum[0], partNum[1] - 1),
        (partNum[0], partNum[1] + 1),
        (partNum[0] - (len(partNum[2]) + 1), partNum[1]),
        (partNum[0] - (len(partNum[2]) + 1), partNum[1] - 1),
        (partNum[0] - (len(partNum[2]) + 1), partNum[1] + 1)
    ]
    for offset in range(1, len(partNum[2]) + 1):
        coordsToCheck.append((partNum[0] - offset, partNum[1] - 1))
        coordsToCheck.append((partNum[0] - offset, partNum[1] + 1))
    
    isCorrect = True
    for coord in coordsToCheck:
        if coord in symbols:
            break
    else:
        isCorrect = False

    if isCorrect:
        result += int(partNum[2])

print(result)
