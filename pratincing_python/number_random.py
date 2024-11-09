import random

print('Bem-vindo ao jogo de adivinhação! Tente adivinhar o número entre 1 e 100.')
number_random = random.randint(1, 100)
attempts = 0
while attempts < 7:

    n = int(input(f'\nDigite seu palpite (tentativa {attempts + 1} de 7):'))

    if n < 0 or n > 100:
        print('Digite um numero entre 0 e 100.')
        continue

    if n == number_random:
        print(f'Congratulations! You matched the number in {attempts + 1} attempts.')
        break
    else:
        attempts += 1
        if n < number_random:
            print(f'\nO número é maior que {n}.')
        else:
            print(f'\nO número é menor que {n}.')

else:
    print('Voce ja atingiu o numero maximo de tentativas')
    
