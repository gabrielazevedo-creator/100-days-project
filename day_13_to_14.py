# higher lower game

# I must create a code that compares two infos and I have to say which one was invented first.
# If I get it right then the game keeps the right guess and compares with a new item.
# If I get it wrong then it's game over.

import random

inventions = {
    "Gunpowder": {
        "year": 850,
        "place": "China",
        "inventor": "Chinese alchemists"
    },
    "Mechanical Clock": {
        "year": 1270,
        "place": "Europe (various regions, especially England & Italy)",
        "inventor": "Unknown (developed gradually)"
    },
    "Printing Press": {
        "year": 1440,
        "place": "Mainz, Germany",
        "inventor": "Johannes Gutenberg"
    },
    "Telescope": {
        "year": 1608,
        "place": "Netherlands",
        "inventor": "Hans Lippershey"
    },
    "Steam Engine": {
        "year": 1712,
        "place": "England",
        "inventor": "Thomas Newcomen"
    },
    "Hot Air Balloon": {
        "year": 1783,
        "place": "France",
        "inventor": "Joseph-Michel and Jacques-Étienne Montgolfier"
    },
    "Photography": {
        "year": 1826,
        "place": "France",
        "inventor": "Joseph Nicéphore Niépce"
    },
    "Typewriter": {
        "year": 1868,
        "place": "United States",
        "inventor": "Christopher Latham Sholes"
    },
    "Radio Transmission": {
        "year": 1895,
        "place": "Italy",
        "inventor": "Guglielmo Marconi"
    },
    "ENIAC (First Computer)": {
        "year": 1945,
        "place": "United States",
        "inventor": "John Presper Eckert and John Mauchly"
    },
    "Wheel": {
        "year": -3500,  # BCE
        "place": "Mesopotamia",
        "inventor": "Unknown"
    },
    "Plow": {
        "year": -3000,  # BCE
        "place": "Mesopotamia",
        "inventor": "Unknown"
    },
    "Sailboat": {
        "year": -3100,  # BCE
        "place": "Egypt",
        "inventor": "Unknown"
    },
    "Paper": {
        "year": 105,
        "place": "China",
        "inventor": "Cai Lun"
    },
    "Compass": {
        "year": 206,
        "place": "China",
        "inventor": "Unknown"
    },
    "Silk Weaving": {
        "year": -2700,  # BCE
        "place": "China",
        "inventor": "Unknown"
    },
    "Concrete": {
        "year": -650,  # BCE
        "place": "Rome",
        "inventor": "Roman Builders"
    },
    "Acupuncture": {
        "year": -100,  # BCE
        "place": "China",
        "inventor": "Unknown"
    },
    "Umbrella": {
        "year": -1000,  # BCE
        "place": "China",
        "inventor": "Unknown"
    },
    "Soap": {
        "year": -2800,  # BCE
        "place": "Babylon",
        "inventor": "Unknown"
    },
    "Eyeglasses": {
        "year": 1286,
        "place": "Italy",
        "inventor": "Unknown"
    },
    "Mechanical Calculator": {
        "year": 1642,
        "place": "France",
        "inventor": "Blaise Pascal"
    },
    "Barometer": {
        "year": 1643,
        "place": "Italy",
        "inventor": "Evangelista Torricelli"
    },
    "Microscope": {
        "year": 1590,
        "place": "Netherlands",
        "inventor": "Zacharias Janssen"
    },
    "Flush Toilet": {
        "year": 1596,
        "place": "England",
        "inventor": "Sir John Harington"
    },
    "Thermometer": {
        "year": 1714,
        "place": "Netherlands",
        "inventor": "Daniel Gabriel Fahrenheit"
    },
    "Steam Pump": {
        "year": 1712,
        "place": "England",
        "inventor": "Thomas Newcomen"
    },
    "Magnetic Compass": {
        "year": 1300,
        "place": "China",
        "inventor": "Unknown"
    },
    "Pendulum Clock": {
        "year": 1656,
        "place": "Netherlands",
        "inventor": "Christiaan Huygens"
    },
    "Light Bulb": {
        "year": 1879,
        "place": "United States",
        "inventor": "Thomas Edison"
    },
    "Telephone": {
        "year": 1876,
        "place": "United States",
        "inventor": "Alexander Graham Bell"
    },
    "Automobile": {
        "year": 1886,
        "place": "Germany",
        "inventor": "Karl Benz"
    },
    "Airplane": {
        "year": 1903,
        "place": "United States",
        "inventor": "Wright Brothers"
    },
    "Penicillin": {
        "year": 1928,
        "place": "United Kingdom",
        "inventor": "Alexander Fleming"
    },
    "Television": {
        "year": 1927,
        "place": "United States",
        "inventor": "Philo Farnsworth"
    },
    "Computer Mouse": {
        "year": 1964,
        "place": "United States",
        "inventor": "Douglas Engelbart"
    },
    "Internet": {
        "year": 1969,
        "place": "United States",
        "inventor": "ARPANET Team"
    },
    "Mobile Phone": {
        "year": 1973,
        "place": "United States",
        "inventor": "Martin Cooper"
    },
    "GPS": {
        "year": 1978,
        "place": "United States",
        "inventor": "U.S. Department of Defense"
    }
}



list_of_used_items = []
score = 0


def generate_random_invention_01(inventions):
    """"This code picks the first random invention."""
    dic_turn_list = list(inventions.keys())  # Here I turn my keys in my dictionary into lists.

    random_pick_01 = random.choice(dic_turn_list)  # Here I pick one random key (that now is a list).
    list_of_used_items.append(random_pick_01)

    chosen_invention_01 = inventions[random_pick_01]  # Here I access all info inside my chosen key list.

    pick_year_01 = chosen_invention_01['year']  # I must do this to access one specific information
    pick_place_01 = chosen_invention_01['place']
    pick_inventor_01 = chosen_invention_01['inventor']

    return random_pick_01, pick_year_01, pick_place_01, pick_inventor_01

def generate_random_invention_02(inventions):
    """"This code picks the second random invention."""
    dic_turn_list = list(inventions.keys())  # Here I turn my keys in my dictionary into lists.

    while True:
        random_pick_02 = random.choice(dic_turn_list)
        if random_pick_02 in list_of_used_items:
            continue
        else:
            list_of_used_items.append(random_pick_02)
            break


    chosen_invention_02 = inventions[random_pick_02]

    pick_year_02 = chosen_invention_02['year']
    pick_place_02 = chosen_invention_02['place']
    pick_inventor_02 = chosen_invention_02['inventor']

    return random_pick_02, pick_year_02, pick_place_02, pick_inventor_02


def generate_new_item(random_pick_01, pick_year_01, pick_place_01, pick_inventor_01):

    # Those two new variable are needed because when I call the 'generate_random_invention' function, it gives me four values,
    # the name, the year, the place and the inventor of the invention,
    # therefore, I need four new variables one for each value, so I use them separately.
    new_name, new_year, new_place, new_inventor  = generate_random_invention_02(inventions)

    # I must declare the global variable first before I change it the way I want, in this case I want to add 1 point.
    global score

    compare2 = input(f'Which one was invented first\n'
                     f'1- {random_pick_01}\n'
                     f'2- {new_name}\n'
                     )
    if compare2 == '1':
        if pick_year_01 < new_year:
            score += 1
            print(
                f'You are right.\nThe {random_pick_01} was invented in {pick_year_01} in {pick_place_01} by {pick_inventor_01}\n'
                f'While the {new_name} was invented in {new_year} in {new_place} by {new_inventor}.')
            # This way I can always update my dictionary of inventions and the limit is updated automatically:
            # If the length of one is equals the other.
            if len(list_of_used_items) >= len(inventions):
                print(f'Game over.\nTotal score: {score}')
                return
            else:
                generate_new_item(random_pick_01, pick_year_01, pick_place_01, pick_inventor_01)
        else:
            print(
                f'You are wrong.\nThe {random_pick_01} was invented in {pick_year_01} in {pick_place_01} by {pick_inventor_01}\n'
                f'While the {new_name} was invented in {new_year} in {new_place} by {new_inventor}.')
            print(f'Total score: {score}')

            return
    if compare2 == '2':
        if new_year < pick_year_01:
            score += 1
            print(
                f'You are right.\nThe {new_name} was invented in {new_year} in {new_place} by {new_inventor}\n'
                f'While the {random_pick_01} was invented in {pick_year_01} in {pick_place_01} by {pick_inventor_01}.')
            if len(list_of_used_items) >= len(inventions):
                print(f'Game over.\nTotal score: {score}')
                return
            else:
                # Here I changed the arguments so the new name and new year are now the ones carried forward.
                generate_new_item(new_name, new_year, new_place, new_inventor)
        else:
            print(
                f'You are wrong.\nThe {random_pick_01} was invented in {pick_year_01} in {pick_place_01} by {pick_inventor_01}\n'
                f'While the {new_name} was invented in {new_year} in {new_place} by {new_inventor}.')
            print(f'Total score: {score}')
            return


def compare_year(random_pick_01,random_pick_02,pick_year_01,pick_year_02,pick_place_01,pick_place_02,pick_inventor_01,pick_inventor_02):
    """"This code compares two inventions."""

    global score
    while True:
        compare = input(f'Which one was invented first\n'
                        f'1- {random_pick_01}\n'
                        f'2- {random_pick_02}\n'
                        )
        if compare == '1':
            if pick_year_01 < pick_year_02:
                score += 1
                print(f'You are right.\nThe {random_pick_01} was invented in {pick_year_01} in {pick_place_01} by {pick_inventor_01}\n'
                      f'While the {random_pick_02} was invented in {pick_year_02} in {pick_place_02} by {pick_inventor_02}.')   # I must include the rest of the info when the person gets it right and wrong as well.
                generate_new_item(random_pick_01, pick_year_01,pick_place_01,pick_inventor_01)
                break
            else:
                print(
                    f'You are wrong.\nThe {random_pick_01} was invented in {pick_year_01} in {pick_place_01} by {pick_inventor_01}\n'
                    f'While the {random_pick_02} was invented in {pick_year_02} in {pick_place_02} by {pick_inventor_02}.')
                print(f'Total score: {score}')
                break
        elif compare == '2':
            if pick_year_02 < pick_year_01:
                score += 1
                print(
                    f'You are right.\nThe {random_pick_02} was invented in {pick_year_02} in {pick_place_02} by {pick_inventor_02}\n'
                    f'While the {random_pick_01} was invented in {pick_year_01} in {pick_place_01} by {pick_inventor_01}.')
                generate_new_item(random_pick_01, pick_year_01,pick_place_01,pick_inventor_01)
                break
            else:
                print(
                    f'You are wrong.\nThe {random_pick_01} was invented in {pick_year_01} in {pick_place_01} by {pick_inventor_01}\n'
                    f'While the {random_pick_02} was invented in {pick_year_02} in {pick_place_02} by {pick_inventor_02}.')
                print(f'Total score: {score}')
                break
        else:
            print('Wrong choice.')
            continue



while True:
    # I have to create those variables outside my function so the 'compare_year' function can get its values.
    random_pick_01, pick_year_01, pick_place_01, pick_inventor_01 = generate_random_invention_01(inventions)
    random_pick_02, pick_year_02, pick_place_02, pick_inventor_02 = generate_random_invention_02(inventions)

    # generate_random_invention_01(inventions) # I don't need to call the functions here, because they are being called above.
    # generate_random_invention_02(inventions)
    # The order of the arguments should match the ones in the function parentheses.
    compare_year(random_pick_01, random_pick_02,pick_year_01, pick_year_02,pick_place_01,pick_place_02,pick_inventor_01,pick_inventor_02)
    play_again = input('Do you want to play again?[Y/N]\n').strip().lower()
    if play_again == 'y':
        list_of_used_items.clear()
        score = 0
        continue
    elif play_again == 'n':
        print('Thanks for playing.')
        break
    else:
        print('Wrong choice.')
        continue
