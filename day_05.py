# Password generator

import random

letters_list = [ "A","B","C","D","E","F","G","H","I","J","K","L","M",
              "N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
              "a","b","c","d","e","f","g","h","i","j","k","l","m",
              "n","o","p","q","r","s","t","u","v","w","x","y","z" ]

symbols_list = ['!','#','$','&','@','?']

numbers_list = ['1','2','3','4','5','6','7','8','9','0']

letters = int(input('How many letters do you want? '))
symbols = int(input('How many symbols do you want? '))
numbers = int(input('How many numbers do you want? '))

password = []

for x in range(letters):
    letter = random.choice(letters_list)
    password.append(letter)

for x in range(symbols):
    symbol = random.choice(symbols_list)
    password.append(symbol)

for x in range(numbers):
    number = random.choice(numbers_list)
    password.append(number)

random.shuffle(password) #Aqui eu usei o random.shuffle para embaralhar o password.
final_password = ''.join(password) #Aqui eu usei o .join para unir todas as unidades que estavam na lista password e tirar os espacos entre eles.
print(final_password)
