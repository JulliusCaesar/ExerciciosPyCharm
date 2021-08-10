time = list()
gols = list()
identificaJogador = dict()
while True:
    identificaJogador.clear()
    identificaJogador['nome'] = str(input('Nome do Jogador: '))
    numPartidas = int(input(f'Quantas partidas {identificaJogador["nome"]} jogou? '))
    gols.clear()
    for contador in range(0, numPartidas):
        gols.append(int(input(f'    Quantos gols na partida {contador + 1}? ')))
    identificaJogador['gols'] = gols[:]
    identificaJogador['total'] = sum(gols)  # Função para Somar
    time.append(identificaJogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in identificaJogador.keys():  # Cabeçalho
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time [busca]["nome"]}: ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print(' << VOLTE SEMPRE >> ')
