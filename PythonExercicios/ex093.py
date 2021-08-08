'''Crie um programa que gerencie o aproveitamento de um jogador de Futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato'''
gols = list()
identificaJogador = dict()
identificaJogador['nome'] = str(input('Nome do Jogador: '))
numPartidas = int(input(f'Quantas partidas {identificaJogador["nome"]} jogou? '))
for contador in range(0, numPartidas):
    gols.append(int(input(f'Quantos gols na partida {contador}? ')))
identificaJogador['gols'] = gols[:]
identificaJogador['total'] = sum(gols)  # Função para Somar
print('-=' * 50)
print(identificaJogador)
print('-=' * 50)
for Key, Value in identificaJogador.items():
    print(f'O Campo {Key} tem o valor {Value}')
print('-=' * 50)
print(f'O jogador {identificaJogador["nome"]} jogou {numPartidas} partidas')
for contador in range(0, numPartidas):  # for i, v in enumerate(identificaJogador['gols']):
    print(f'=> Na partida {contador}, fez {gols[contador]} gols. ')  # print(f' => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {identificaJogador["total"]}')
