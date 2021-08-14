'''Faça um programa que tenha a função chamada maior(), que receba varios parâmetros com valores inteiros. Seu progra
ma tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep


def maior(* num):
    maiornum = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    if num != 0:
        for valor in num:
            sleep(0.5)
            print(f'{valor} ', end='')
            if valor > maiornum:
                maiornum = valor
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {maiornum}.')
    else:
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {maiornum}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()