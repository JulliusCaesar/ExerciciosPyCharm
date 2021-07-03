'''Refaça o desafio 009, mostrando a tabuada de um número que o usuario escolher so que agora ultilizando um laço FOR'''
print('====='*8, 'EX049', '====='*8)
n = int(input('Digite o número que você deseja ver  Tabuada: '))
print('-='* 8)
for c in range(1, 11):
    print('{}  x {:2} = {}'.format(n, c, n * c))
print('-='* 8)