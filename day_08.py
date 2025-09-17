# Caesar Cipher

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encode():
    encoded_message = ''
    message = input('Type the message to encrypt: ').strip().upper()
    shift = int(input('Type the number of shifts: ').strip())
    for position, value in enumerate(message):
        if value in alphabet:

            position_in_alphabet = alphabet.index(value)

            encoded_message += alphabet[(position_in_alphabet + shift) % 26]
            #
            # In this part above, I have to add the shift first, then I make the modulo of the amount of letters in the alphabet.
            # Z is the 25th letter, since the program starts to count in zero.
            # Therefore, 25(z) + 1(shift) modulo of 26(total amount of letters) = 0(A)
            #
        else:
            encoded_message += value

    print(encoded_message)



def decode():
    decoded_message = ''
    encrypted_message = input('Type the secret message to be decoded: ').strip().upper()
    shift_2 = int(input('How many shifts did this message use? ').strip())

    for position, value in enumerate(encrypted_message):
        if value in alphabet:
            position_in_alphabet = alphabet.index(value)
            decoded_message += alphabet[(position_in_alphabet - shift_2) % 26]
        else:
            decoded_message += value

    print(decoded_message)


while True:
    choice = input('1- Encode, 2- Decode, 3- Exit\n')
    if choice == '1':
        encode()
    elif choice == '2':
        decode()
    elif choice == '3':
        print('Goodbye!')
        break
    else:
        print('Choose a valid option.')
        continue
