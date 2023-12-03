#!/bin/python3
houses = set()
santaCoordinates = (0, 0)
roboSantaCoordinates = (0, 0)
santaOrRoboSanta = True

for direction in open('data.txt', 'r').read():
    if santaOrRoboSanta:
        santaOrRoboSanta = False
        if direction == '^':
            santaCoordinates = (santaCoordinates[0], santaCoordinates[1] + 1)
        elif direction == 'v':
            santaCoordinates = (santaCoordinates[0], santaCoordinates[1] - 1)
        elif direction == '>':
            santaCoordinates = (santaCoordinates[0] + 1, santaCoordinates[1])
        elif direction == '<':
            santaCoordinates = (santaCoordinates[0] - 1, santaCoordinates[1])
        houses.add(santaCoordinates)
    else:
        santaOrRoboSanta = True
        if direction == '^':
            roboSantaCoordinates = (roboSantaCoordinates[0], roboSantaCoordinates[1] + 1)
        elif direction == 'v':
            roboSantaCoordinates = (roboSantaCoordinates[0], roboSantaCoordinates[1] - 1)
        elif direction == '>':
            roboSantaCoordinates = (roboSantaCoordinates[0] + 1, roboSantaCoordinates[1])
        elif direction == '<':
            roboSantaCoordinates = (roboSantaCoordinates[0] - 1, roboSantaCoordinates[1])
        houses.add(roboSantaCoordinates)
        
print(len(houses))
