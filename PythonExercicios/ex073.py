'''Crie um TUPLA preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileira de futebol, na ordem
de colocação. Depois mostre a) Apenas os 5 primeiros colocados, b) os últimos 4 colocados da tabela, c) Uma lista
com times em ordem alfabética d) Em que posição na tabela está o time da Chapecoense'''

tabela = ('Corintnhians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético',
          'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba',
          'Avai', 'Ponte Preta', 'Atlético-GO')
print('-='*15)
print(f'Lista de Times do Brasileirão: {tabela}')
print('-='*15)
print(f'Os 5 primeiro são: {tabela[:5]}')
print('-='*15)
print(f'oS 4 últimos são: {tabela[-4:]}')
print('-='*15)
print(f'Times em Ordem Alfabética: {sorted(tabela)}')
print('-='*15)
print('O Chapecoense está na {}ª Posição.'.format(tabela.index('Chapecoense')+1))
# print(f'O Chapecoense está na {tabela.index("Chapecoense")}ª Posição.') TEM QUE USAR ASPAS DUPLAS