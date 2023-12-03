#!/bin/python3
houses = set()
coordinates = (0, 0)
for direction in open('data.txt', 'r').read():
    if direction == '^':
        coordinates = (coordinates[0], coordinates[1] + 1)
    elif direction == 'v':
        coordinates = (coordinates[0], coordinates[1] - 1)
    elif direction == '>':
        coordinates = (coordinates[0] + 1, coordinates[1])
    elif direction == '<':
        coordinates = (coordinates[0] - 1, coordinates[1])
    houses.add(coordinates)
print(len(houses))
