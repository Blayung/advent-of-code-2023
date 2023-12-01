#!/bin/python3
lines = [list(i) for i in open('data.txt', 'r').readlines()]
result = 0
for line in lines:
    for char in line:
        try:
            firstDigit = int(char)
            break
        except ValueError:
            pass
    for char in reversed(line):
        try:
            secondDigit = int(char)
            break
        except ValueError:
            pass
    result += firstDigit * 10 + secondDigit

print(result)
