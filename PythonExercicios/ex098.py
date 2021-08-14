'''Faça um programa que tenha uam função chamada contador(), que receba três parâmetros: inicio, fim  e passo
e realize a contagem. Seu programa tem que realizar três contagens através da função criada: a) de 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2, c) uma contagem personalizada'''
from time import sleep


def contador(inicio, fim, passo):

    print('-=' * 15)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    for contagem in range(inicio, fim + 1, passo):
        sleep(1)
        print(f'{contagem} ', end='')
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)
print("-=" * 15)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(inicio, fim, passo)
