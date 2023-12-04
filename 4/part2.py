#!/bin/python3
ogCards = [line.split()[2:] for line in open('data.txt', 'r').readlines()]

result = 0
cards = ogCards
while True:
    result += len(cards)

    cardsToCopy = []
    for cardNum, card in enumerate(cards, 1):
        wonCards = 0
        winningNums = []
        leftOrRight = True
        for part in card:
            if part == '|':
                leftOrRight = False
                continue
            if leftOrRight:
                winningNums.append(part)
            elif part in winningNums:
                wonCards += 1
        cardsToCopy.extend(range(cardNum, cardNum + wonCards))

    if len(cardsToCopy) == 0:
        print(result)
        break

    cards = []
    for cardToCopy in cardsToCopy:
        try:
            cards.append(ogCards[cardToCopy])
        except IndexError:
            break
