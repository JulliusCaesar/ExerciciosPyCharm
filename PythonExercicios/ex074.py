'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem
de números gerados e também indique o menor e o maior valor que estão na tupla.'''
from random import randint
aleatorio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: {aleatorio}')
maior = menor = aleatorio[0]
for c in range(0, len(aleatorio)):
    if aleatorio[c] > maior:
        maior = aleatorio[c]
    elif aleatorio[c] < menor:
        menor = aleatorio[c]
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
