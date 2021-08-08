'''Crie um programa onde 4 jogadores joguem um dado e tenham resulatdos aleátorios. Guarde esses resultados
em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ranking = list()
print('Valores Sorteados: ')
for key, value in jogo.items():
    print(f'O {key} tirou {value}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  # o valor 1 pega os randint, caso fosse 0 seria o jogador1 assim por diante
print('-=' * 30)
print('  == RANKING DOS JOGADORES == ')
for i, v in enumerate(ranking):
    print(f'  {i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
