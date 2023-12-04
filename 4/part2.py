#!/bin/python3
nextCards = []
for cardNum, card in enumerate([line.split()[2:] for line in open('data.txt', 'r').readlines()]):
    correctNumsAmount = 0
    winningNums = []
    leftOrRight = True
    for part in card:
        if part == '|':
            leftOrRight = False
            continue
        if leftOrRight:
            winningNums.append(part)
        elif part in winningNums:
            correctNumsAmount += 1
    nextCards.append(range(cardNum + 1, cardNum + correctNumsAmount + 1))

result = 0

def processCards(cards):
    global result
    for card in cards:
        try:
            processCards(nextCards[card])
            result += 1
        except IndexError:
            break

processCards(range(0, len(nextCards)))

print(result)
