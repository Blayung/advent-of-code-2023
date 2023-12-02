#!/bin/python3
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def convert(num):
    if num == '0':
        return 0
    elif num == '1' or num == 'one':
        return 1
    elif num == '2' or num == 'two':
        return 2
    elif num == '3' or num == 'three':
        return 3
    elif num == '4' or num == 'four':
        return 4
    elif num == '5' or num == 'five':
        return 5
    elif num == '6' or num == 'six':
        return 6
    elif num == '7' or num == 'seven':
        return 7
    elif num == '8' or num == 'eight':
        return 8
    elif num == '9' or num == 'nine':
        return 9

result = 0
for line in open('data.txt', 'r').readlines():
    i = 1
    while True:
        for digit in digits:
            if digit in line[:i]:
                result += convert(digit) * 10
                break
        else:
            i += 1
            continue
        break

    i = -1
    while True:
        for digit in digits:
            if digit in line[i:]:
                result += convert(digit)
                break
        else:
            i -= 1
            continue
        break
    
print(result)
