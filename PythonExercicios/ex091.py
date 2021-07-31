'''Crie um programa onde 4 jogadores joguem um dado e tenham resulatdos aleátorios. Guarde esses resultados
em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado'''
from random import randint
from time import sleep
jogo = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
print('Valores Sorteados: ')
for key, value in jogo.items():
    print(f'O {key} tirou {value}')
    sleep(1)
print('Ranking dos Jogadores: ')
