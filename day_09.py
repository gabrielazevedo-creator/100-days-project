# Blind Auction

import random

items = ['Signed First Edition Book', 'Handcrafted Wooden Chess Set', 'Antique Pocket Watch',
         'Limited Edition Vinyl Record', 'Vintage Leather Motorcycle Jacket',
         ]


buyers = {}

winner = ''
highest_bid = 0

while len(items) != 0:

    chosen_item = random.choice(items)
    print(f'Ladies and gentlemen, we’re starting the bidding of a/an {chosen_item}.')

    buyers.clear()

    while True:
        name = input('What is the gentleman / lady\'s name?\n').strip().title()
        bid = int(input(f'Mr./Mrs. {name}, how much do you bid for {chosen_item} item?\n').strip())
        buyers[name] = bid
        keep_bidding = input('Are there more ladies or gentlemen to bid? [Y/N]\n').strip().lower()
        if keep_bidding == 'y':
            print('\n' * 50)
            continue
        else:
            break
    for key in buyers:

        if buyers[key] > highest_bid:
            highest_bid = buyers[key]
            winner = key
    print(f'{chosen_item} sold for ${highest_bid} to Mr./Mrs. {winner}')
    highest_bid = 0
    items.remove(chosen_item)

print('Ladies and gentlemen, all items were sold out. The auction is over.')
