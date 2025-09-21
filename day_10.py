# Calculator



def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2



operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


print('----------')
print('Calculator')
print('----------')


value = 0


while True:
    n1 = round(float((input('Enter the first number:\n').strip().lower())),2)

    value += n1

    while True:
        sign = input(f'What would you like to do with {value}?\nAdd (+)\nSubtract (-)\nMultiply (*)\nDivide (/)\nBack (b)\n').strip()
        if sign == 'b':
            break
        n2 = round(float(input('Enter the other number: ').strip()))
        answer = operations[sign](n1, n2)
        print(f'{n1} {sign} {n2} = {round(answer, 2)}')
        value = answer
        choice = input('Would you like to continue this operation [Y] or change it [N]?\n').strip().lower()
        n1 = value
        if choice == 'y':
            continue
        else:
            value = 0
            break
