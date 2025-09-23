# Blackjack
# I must finish this project


import random

cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

def deal_card():
    card = random.choice(cards)
    return card


def total_cards(player_cards):
    if sum(player_cards) == 21 and len(player_cards) == 2:
        return 0
    if 11 in player_cards and sum(player_cards) > 21:
        player_cards.remove(11)
        player_cards.append(1)

    return sum(player_cards)

def total_dealer_cards(dealer_cards):
    if sum(dealer_cards) == 21 and len(dealer_cards) == 2:
        return 0
    if 11 in dealer_cards and sum(dealer_cards) > 21:
        dealer_cards.remove(11)
        dealer_cards.append(1)

    return sum(dealer_cards)



player_cards = []
dealer_cards = []

letter_card = ['','','','','','',]
dealer_letter_card = ['','','','','','']




# drawing player cards
for draw in range(2):
    pick = deal_card()
    if pick in ['J', 'Q', 'K']:
        if draw == 0:
            if letter_card[0] == '':
                letter_card[0] = pick
                player_cards.append(10)
        if draw == 1:
            if letter_card[1] == '':
                letter_card[1] = pick
                player_cards.append(10)
    if pick == 'A':
        if draw == 0:
            if letter_card[0] == '':
                letter_card[0] = pick
                player_cards.append(11)
        if draw == 1:
            if letter_card[1] == '':
                letter_card[1] = pick
                player_cards.append(11)
    if pick not in ['A', 'J', 'Q', 'K']:
        player_cards.append(pick)



print(f"Player cards = {total_cards(player_cards)}\n{letter_card[0] if letter_card[0] != '' 
else player_cards[0]} {letter_card[1] if letter_card[1] != '' else player_cards[1]}")



# drawing dealer cards
for draw in range(2):
    pick = deal_card()
    if pick in ['J', 'Q', 'K']:
        if draw == 0:
            if dealer_letter_card[0] == '':
                dealer_letter_card[0] = pick
                dealer_cards.append(10)
    if draw == 1:
        if dealer_letter_card[1] == '':
            dealer_letter_card[1] = pick
            dealer_cards.append(10)
    if pick == 'A':
        if draw == 0:
            if dealer_letter_card[0] == '':
                dealer_letter_card[0] = pick
                dealer_cards.append(11)
        if draw == 1:
            if dealer_letter_card[1] == '':
                dealer_cards[1] = pick
                dealer_cards.append(11)
    if pick not in ['A', 'J', 'Q', 'K']:
        dealer_cards.append(pick)


print(f"Dealer cards = {'*'}\n{dealer_letter_card[0] if dealer_letter_card[0] != '' 
else dealer_cards[0]} {'*'}")

# print(f"Dealer cards = {total_dealer_cards(dealer_cards)}\n{dealer_letter_card[0] if dealer_letter_card[0] != ''
# else dealer_cards[0]} {dealer_cards[1] if dealer_letter_card[1] != '' else dealer_cards[1]}")

count = 2

print('---------------------------')
while True:
    hit = input('1- Hit\n2- Stand\n')
    if hit == '1':
        pick = deal_card()
        if pick in ['J', 'Q', 'K']:
            if letter_card[count] == '':
                letter_card[count] = pick
                player_cards.append(10)
                count += 1

        if pick == 'A':
            if letter_card[count] == '':
                letter_card[count] = pick
                player_cards.append(11)

        if pick not in ['A', 'J', 'Q', 'K']:
            player_cards.append(pick)
    print(f"Player cards = {total_cards(player_cards)}\n{letter_card[0] if letter_card[0] != ''
    else player_cards[0]} {letter_card[1] if letter_card[1] != '' else player_cards[1]} {letter_card[2]}")

    if hit == '2':
        break

print(f"Player cards = {total_cards(player_cards)}\n{letter_card[0] if letter_card[0] != '' 
else player_cards[0]} {letter_card[1] if letter_card[1] != '' else player_cards[1]} "
      f"{letter_card[2] if letter_card[2] != '' else player_cards[2]}") # I have to make a way to add more print equivalent to the amount of cards
