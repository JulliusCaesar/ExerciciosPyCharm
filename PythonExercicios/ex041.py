'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade: - até 9 anos MIRIM. - Até 14 anos INFANTIL. - Até 19 anos JUNIOR. - Até 20 anos Sênior
 - Acima MASTER'''
from datetime import date
print('\033[33m===\033[m'*20, 'EX041', '\033[33m===\033[m'*20)
print('==='*15, ' Confederação Nacional de Natação ', '==='*15)
print('==='*15, '    Descubra sua categoria    ', '==='*15)
nasc = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print('Você tem {} anos e sua categoria é MIRIM!'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e sua categoria é INFANTIL!'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e sua categoria é JUNIOR!'.format(idade))
elif idade <= 25:
    print('Você tem {} anos e sua categoria é SÊNIOR!'.format(idade))
else:
    print('Você tem {} anos e sua categoria é MASTER!'.format(idade))