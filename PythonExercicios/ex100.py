'''Faça um programa que tenha uma llista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira
função vai sortear 5 números e vai colocá los dentro da lista e a segunda função vai mostrar a soma entre todos os
valores pares sorteados pela função anterior'''
from random import randint
from time import sleep
numeros = list()


def sorteio():
    lista = [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)]
    print('Sorteando 5 valores da Lista: ', end='')
    for passagem in range(0, len(lista)):
        print(f'{lista[passagem]} ', end='')
        sleep(0.5)
    print(' PRONTO!')
    numeros = lista[:]


def somaPar():
    soma = 0
    for controle in range(0, len(numeros)):
        if numeros[controle] % 2 == 0:
            soma += numeros[controle]
    print(f'Somando os valores pares de {numeros}, temos {soma}')


sorteio()
somaPar()
