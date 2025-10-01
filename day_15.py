from time import sleep


# # By using this 'r' before the quotation marks, I tell Python that it must treat everything inside the quotation as a string.
coffee_art = r"""
( (
    ) )
  ........
  |      |]
  \      /    
   `----'
"""
latte_art = r"""
  .-~~-.
,|`-__-'|
||      |
`|      |  
  `-__-'
"""
cappuccino_art = r"""
 .=%%=.
,|`=%%='|
||      |
`|      |  
  `-__-'
"""

menu = {
    'espresso': {'price': 1.50,
                 'water': 50,
                 'coffee': 18,
                 'milk': 0},
    'latte': {'price': 2.50,
                 'water': 200,
                 'coffee': 24,
                 'milk': 150},
    'cappuccino': {'price': 3.00,
                 'water': 250,
                 'coffee': 24,
                 'milk': 100}
}


def menu_options():
    choose = input(f'Menu:\n'
                   f'1- Espresso   - $1.50\n'
                   f'2- Latte      - $2.50\n'
                   f'3- Cappuccino - $3.00\n'
                   f'4- Insert coins\n'
                   f'5- Return inserted coins\n'
                   f'6- Print resources\n'
                   f'7- Exit\n')
    return choose

resource = {'water': 300, 'milk': 200, 'coffee': 100}

# penny = 0   # I'm not using those variables anymore, because their value was being carried even after I spent my whole money.
# nickel = 0
# dime = 0
# quarter = 0

total = round(0,2)

profit = 0

def coins(total):
    insert_penny = int(input('Insert pennies (0.01): ').strip())
    # penny += insert_penny
    insert_nickel = int(input('Insert nickels (0.05): ').strip())
    # nickel += insert_nickel
    insert_dime = int(input('Insert dimes (0.10): ').strip())
    # dime += insert_dime
    insert_quarter = int(input('Insert quarters (0.25): ').strip())
    # quarter += insert_quarter

    total += round((insert_penny * 0.01) + (insert_nickel * 0.05) + (insert_dime * 0.10) + (insert_quarter * 0.25), 2)
    print(f'Total: ${total}')
    return total




while True:
    choose = menu_options()

    # print(f'Total: ${total}')
    # penny, nickel, dime, quarter, total = coins(penny, nickel, dime, quarter, total)


    if choose == '1':                           # Espresso was the chosen beverage
        if total < menu['espresso']['price']:   # Not enough coins were inserted
            print('Not enough coins.')
            continue
        else:                                   # The right amount of coins was inserted
            if resource['coffee'] < menu['espresso']['coffee'] or resource['water'] < menu['espresso']['water']: # There's not enough resource
                print('Out of resources. PLease refill it.')
                total = 0
                print('Coins returned.')
                continue
            else:
                total = round(total - menu['espresso']['price'],2) # I had to change this to obtain a round number
                resource['water'] -= menu['espresso']['water']
                resource['coffee'] -= menu['espresso']['coffee']
                profit += menu['espresso']['price']
                print(f'Your change: ${round(total, 2)}')
                total = 0
                sleep(0.5)
                print('Wait...')
                sleep(0.5)
                print('Enjoy your espresso.')
                print(coffee_art)


    if choose == '2':                        # Latte was the chosen beverage
        if total < menu['latte']['price']:   # Not enough coins were inserted
            print('Not enough coins.')
            continue
        else:                                   # The right amount of coins was inserted
            if resource['coffee'] < menu['latte']['coffee'] or resource['water'] < menu['latte']['water'] or resource['milk'] < menu['latte']['milk']: # There's not enough resource
                print('Out of resources. PLease refill it.')
                total = 0
                print('Coins returned.')
                continue
            else:
                total = round(total - menu['latte']['price'],2)
                resource['water'] -= menu['latte']['water']
                resource['coffee'] -= menu['latte']['coffee']
                resource['milk'] -= menu['latte']['milk']
                profit += menu['latte']['price']
                print(f'Your change: ${round(total,2)}')
                total = 0
                sleep(0.5)
                print('Wait...')
                sleep(0.5)
                print('Enjoy your latte.')
                print(latte_art)


    if choose == '3':                             # Cappuccino was the chosen beverage
        if total < menu['cappuccino']['price']:   # Not enough coins were inserted
            print('Not enough coins.')
            continue
        else:                                   # The right amount of coins was inserted
            if resource['coffee'] < menu['cappuccino']['coffee'] or resource['water'] < menu['cappuccino']['water'] or resource['milk'] < menu['cappuccino']['milk']: # There's not enough resource
                print('Out of resources. PLease refill it.')
                total = 0
                print('Coins returned.')
                continue
            else:
                total = round(total - menu['cappuccino']['price'],2)
                resource['water'] -= menu['cappuccino']['water']
                resource['coffee'] -= menu['cappuccino']['coffee']
                profit += menu['cappuccino']['price']
                print(f'Your change: ${round(total, 2)}')
                total = 0
                sleep(0.5)
                print('Wait...')
                sleep(0.5)
                print('Enjoy your cappuccino.')
                print(cappuccino_art)

    if choose == '4':
        print(f'Total: ${round(total,2)}')
        total = coins(round(total,2))

    if choose == '5':
        print(f'The total change of ${round(total,2)} was returned ')
        total = 0
        print(f'Total: ${round(total,2)}')
        continue

    if choose == '6':
        print('Resources:')

        # I have to use .items, otherwise the for loop only catches the keys, not the values as well.
        for key, value in resource.items():
            sleep(0.4)
            if key == 'coffee':
                print(f'{key}: {value}g')
            else:
                print(f'{key}: {value}ml')
        sleep(0.4)
        print('_______________')
        print(f'Profit: ${profit}')
        sleep(0.4)
        continue

    if choose == '7':
        print('Thank you for enjoying our coffee machine.')
        break
