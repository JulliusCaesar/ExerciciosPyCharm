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
        identidade['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    if identidade['sexo'] == 'F':
        mulheres.append(identidade['nome'])
    identidade['idade'] = int(input('Idade: '))
    somaIdade += identidade['idade']
    listaIdentidade.append(identidade.copy())
    del identidade['nome']
    del identidade['sexo']
    del identidade['idade']
    resp = str(input('Gostaria de continuar [S/N]: ')).strip().upper()
    somaCont += 1
    while resp not in 'SN':
        resp = str(input('Gostaria de continuar [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 40)
mediaIdade = somaIdade / somaCont
print(f'- O grupo tem {mediaIdade} pessoas.')
print(f'- As mulheres cadastradas foram: {mulheres}')
print('- Lista das pessoas que estão acima da média:')
