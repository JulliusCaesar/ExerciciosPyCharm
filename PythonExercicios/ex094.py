'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final mostre: a) Quantas pessoas foram cadastradas, b) A média de idade do
grupo. c) Uma lista com todas as mulheres. D) Uma lista com todas as pessoas com idade acima da média.'''
identidade = dict()
listaIdentidade = list()
mulheres = list()
somaCont = somaIdade = mediaIdade = 0
while True:
    identidade['nome'] = str(input('Nome: '))
    identidade['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    while identidade['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        identidade['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    if identidade['sexo'] == 'F':
        mulheres.append(identidade['nome'])
    identidade['idade'] = int(input('Idade: '))
    somaIdade += identidade['idade']
    listaIdentidade.append(identidade.copy())
    del identidade['nome']   #
    del identidade['sexo']   #  Poderia ter usado identidade.clear()
    del identidade['idade']  #
    resp = str(input('Quer continuar [S/N]: ')).strip().upper()
    somaCont += 1
    while resp not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 40)
mediaIdade = somaIdade / somaCont
print(f'- Ao todo temos {somaCont} pessoas cadastradas.')
print(f'- A média de idade {mediaIdade} anos.')
print(f'- As mulheres cadastradas foram: {mulheres}')
print('- Lista das pessoas que estão acima da média:')
for p in listaIdentidade:
    if p['idade'] >= mediaIdade:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')