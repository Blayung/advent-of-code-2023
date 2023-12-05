#!/bin/python3
lines = open('data.txt', 'r').readlines()

result = -1

for seed in [int(line) for line in lines[0].split(' ')[1:]]:
    num = seed

    for map in [
        [[int(num) for num in line.split(' ')] for line in lines[3:38]],
        [[int(num) for num in line.split(' ')] for line in lines[41:64]],
        [[int(num) for num in line.split(' ')] for line in lines[67:100]],
        [[int(num) for num in line.split(' ')] for line in lines[103:148]],
        [[int(num) for num in line.split(' ')] for line in lines[151:179]],
        [[int(num) for num in line.split(' ')] for line in lines[182:212]],
        [[int(num) for num in line.split(' ')] for line in lines[214:251]]
    ]:
        for mapEntry in map:
            if num in range(mapEntry[1], mapEntry[1] + mapEntry[2] + 1):
                num += mapEntry[0] - mapEntry[1]
                break

    result = num if result == -1 else min(result, num)

print(result)
