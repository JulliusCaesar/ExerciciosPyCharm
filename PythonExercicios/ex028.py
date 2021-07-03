''' Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
 tentar descobrir qual foi o número escolhido pelo Computador. O programa deverá escrever na tela se o usuário
 venceu ou perdeu!'''
import random
from time import sleep
print('\033[30m=====\033[m'*15, 'EX028', '\033[30m=====\033[m'*15)
num = random.randint(0, 5)
print('\033[34m-=-\033[m'*50)
print('\033[35m================ Pensei em um número de 0 a 5 consegue Adivinhar????? =============\033[m')
print('\033[34m-=-\033[m'*50)
adv = int(input('Diga em que número pensei? '))
print('\033[31mPROCESSANDO..........\033[m')
sleep(2)
if adv == num:
    print('\033[34mParabéns Você Venceu!!! Eu pensei no Número {}!!\033[m'.format(num))
else:
    print('\033[31mInfelizmente você Perdeu!! Eu pensei no Número {}!!\033[m'.format(num))
