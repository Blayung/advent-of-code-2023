#!/bin/python3
hands = []
for line in open('data.txt', 'r').readlines():
    hand = line.split(' ')
    hands.append((hand[0], int(hand[1].rstrip('\n'))))

sortedHands = [[], [], [], [], [], [], []]

for hand in hands:
    cardCounts = []
    for card in hand[0]:
        for cardCount in cardCounts:
            if cardCount[0] == card:
                break
        else:
            cardCounts.append((card, hand[0].count(card)))

    for cardCount in cardCounts:
        if cardCount[1] == 5:
            sortedHands[0].append(hand)
            break
        if cardCount[1] == 4:
            sortedHands[1].append(hand)
            break
        if cardCount[1] == 3:
            if len(cardCounts) == 2:
                sortedHands[2].append(hand)
            else:
                sortedHands[3].append(hand)
            break
        if cardCount[1] == 2:
            if len(cardCounts) == 3:
                sortedHands[4].append(hand)
            else:
                sortedHands[5].append(hand)
            break
    else:
        sortedHands[6].append(hand)
    
print(sortedHands)

# TODO: SORT THEM BY SINGULAR CARDS
