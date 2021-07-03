'''Faça um programa que leia o sexo de uma pessoa, mas só aceite valores 'M' ou 'F'. Caso esteja errado, peça a digitação
 novamente até ter um valor correto.'''
print('{:=^80}'.format('EX057'))
s = ''
while 'M' != s != 'F':
    s = str(input('Digite seu sexo [M/F]: ')).strip().upper()
    if s == 'M':
        print('Você digitou o Sexo Masculino!')
    if s == 'F':
        print('Você digitou o Sexo Feminino!')
    if 'M' != s != 'F':
        print('Voc~e digitou um sexo inválido!!')
print('\n\033[34mFim\033[m')