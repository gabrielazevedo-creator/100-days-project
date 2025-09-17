# Hangman
import random

lista_de_palavras = ['LARANJA', 'CACHORRO', 'GATO', 'GUANABARA','DESENVOLVEDOR' ]

forca_0 = '''
+---+
  |   |
      |
      |
      |
      |
=========
'''
forca_1 = '''
 +---+
  |   |
  O   |
      |
      |
      |
=========
'''
forca_2 = '''
+---+
  |   |
  O   |
  |   |
      |
      |
=========
'''
forca_3 = '''
+---+
  |   |
  O   |
 /|   |
      |
      |
=========
'''
forca_4 = '''
 +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
'''

forca_5 = '''
+---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
'''
forca_6 = '''
+---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
'''

forcas = [forca_0, forca_1, forca_2, forca_3, forca_4, forca_5, forca_6]


palavra_secreta = random.choice(lista_de_palavras)
lista_de_letras_usadas = []
palavra_da_forca = []
len_da_palavra_secreta = len(palavra_secreta)
letras_usadas = []
vidas_restantes = 6

for x in range(len_da_palavra_secreta):
    palavra_da_forca.append('_')

palavra_da_forca_limpa = ' '.join(palavra_da_forca)

print(forca_0)
print(palavra_da_forca_limpa)

condicao_para_perder = 0

condicao = False
while condicao == False:
    print(f'Vidas restantes: {vidas_restantes}')
    letra_escolhida = input('Escolha uma letra: ').strip().upper()
    if len(letra_escolhida) != 1:
        print('Escolha apenas uma letra.')
        continue
    else:
        if letra_escolhida in palavra_secreta:
            if letra_escolhida in letras_usadas:
                print('Voce ja usou esta letra, escolha outra.')
                continue
            else:
                letras_usadas.append(letra_escolhida)
            for posicao, letra in enumerate(palavra_secreta):  #Aqui o enumerate permite usar no FOR LOOP tanto o 'posicao' quanto o 'letra', uma vez que ele verifica a posicao e o que ha nela.
                if letra_escolhida == letra:
                    palavra_da_forca[posicao] = letra_escolhida
                    if '_' not in palavra_da_forca:
                        condicao = True
                        print('----------------------')
                        print('Parabens, voce ganhou!')
                        print('----------------------')
                else:
                    continue
        else:
            print(f'A letra {letra_escolhida} nao esta na palavra secreta. Tente outra.')
            condicao_para_perder += 1
            vidas_restantes -= 1
            print(forcas[condicao_para_perder])
            if condicao_para_perder == 6:
                print('Voce perdeu, enforcado!')
                break
    palavra_da_forca_limpa = ' '.join(palavra_da_forca)
    print(palavra_da_forca_limpa)
