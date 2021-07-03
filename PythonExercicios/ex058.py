'''Melhore o jogo do desafio 28 onde o computador vai pensar em um número entre 0 a 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
from time import sleep
print('{:=^80}'.format('EX058'))
acerto = ''
cont = 0
while acerto != 'F':
    num = randint(1, 10)
    print('\033[34m-=-\033[m' * 50)
    print('\033[35m================ Pensei em um número de 1 a 10 consegue Adivinhar????? =============\033[m')
    print('\033[34m-=-\033[m' * 50)
    adv = int(input('Diga em que número eu pensei: '))
    print('\033[31mPROCESSANDO\033[m', end='')
    sleep(0.5)
    print('...', end='')
    sleep(0.5)
    print('...', end='')
    sleep(0.5)
    print('...')
    sleep(0.5)
    cont += 1
    if adv == num:
        print('\033[34mParabéns Você Venceu!!! Eu pensei no Número {}!!\033[m'.format(num))
        acerto = 'F'
    else:
        print('Você ERROU!!!!')
        print(("\nTENTE DENOVO!!!!!"))
print('Você tentou {} vezes.'.format(cont))
