'''Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador.'''

gols = list()
listaJogadores = list()
identificaJogador = dict()
somaGols = 0
while True:
    identificaJogador['nome'] = str(input('Nome do Jogador: '))
    numPartidas = int(input(f'Quantas partidas {identificaJogador["nome"]} jogou? '))
    for contador in range(0, numPartidas):
        gols.append(int(input(f'Quantos gols na partida {contador}? ')))
        somaGols += gols[contador]
    identificaJogador['gols'] = gols[:]
    identificaJogador['total'] = somaGols
    listaJogadores.append(identificaJogador.copy())
    del gols[:]
    del identificaJogador['nome']
    del identificaJogador['gols']
    del identificaJogador['total']
    somaGols = 0
    resp = str(input('Gostaria de continuar [S/N]: ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Gostaria de continuar [S/N]: ')).strip().upper()
    if resp == 'N':
        break
    print('---' * 20)
print('-=' * 40)
print(f'{"cod ":<4}{"Nome":<10}{"Gols":>4}{"Total":>15}')
print('-' * 46)
for i, a in enumerate(listaJogadores):
    print(f'{i:<4}{a["nome"]:<10}{a["gols"]}{a["total"]:>10}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar dados de qual Jogador? '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {listaJogadores[opc]["nome"]}')
    for contador in range(0, numPartidas ):
        print(f'No jogo {contador}, fez {listaJogadores[opc]["gols"][contador]} gols. ')
print('<<< VOLTE SEMPRE >>>')
