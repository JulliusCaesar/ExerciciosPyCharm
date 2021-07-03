'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0
com uma pausa de 1 segundo entre elas'''
print('====='*8, 'EX046', '====='*8)
from time import sleep
print('=-'*15, ' Contagem Regressiva ', '=-'*15)
for c in range(10, -1, -1):
    sleep(1)
    print('=-'*c, c)
print('\033[31mFELIZ ANO NOVO!!!\033[m')