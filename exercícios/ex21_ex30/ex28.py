import random
from time import sleep

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')

n = random.randint(0, 5)
result = int(input("Em que número eu pensei? "))

print('Processando...')
sleep(2)
if result == n:
    print('Parabéns! Você acertou!')
else:
    print(f'Você errou! Eu pensei no número {n}.')
