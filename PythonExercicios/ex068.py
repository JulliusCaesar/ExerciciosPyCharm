'''Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER.
mostando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
VIT = 0
while True:
    print('=-='*20)
    print('VAMOS JOGAR PAR OU IMPAR')
    print('=-='*20)
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    escolha = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    while escolha not in 'PpIi':
        escolha = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    soma = jogador + computador
    if escolha == 'P':
        if soma % 2 == 0:
            print('---'*30)
            print(f'Você jogou {jogador} e o Computador {computador}. Total de {soma} DEU PAR')
            print('---' * 30)
            print('Você VENCEU!!')
            print('Vamos jogar novamente......')
            VIT += 1
        else:
            print(f'Você jogou {jogador} e o Computador {computador}. Total de {soma} DEU IMPAR')
            print('Você PERDEU!')
            print('=-='*20)
            print(f'GAME OVER! Você venceu {VIT}')
            break
    if escolha == 'I':
        if soma % 2 == 1:
            print('---' * 30)
            print(f'Você jogou {jogador} e o Computador {computador}. Total de {soma} DEU IMPAR')
            print('---' * 30)
            print('Você VENCEU!!')
            print('Vamos jogar novamente......')
            VIT += 1
        else:
            print(f'Você jogou {jogador} e o Computador {computador}. Total de {soma} DEU PAR')
            print('Você PERDEU!')
            print('=-=' * 20)
            print(f'GAME OVER! Você venceu {VIT}')
            break
