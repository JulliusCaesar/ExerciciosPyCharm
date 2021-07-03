'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: - se ele ainda vai se alistar
ao serviço militar. - se é a hora de se alistar. - se já passou do tempo de alistamento. Seu programa também deverá
mostrar o tempo que falta ou que passou o prazo'''
from datetime import date
print('\033[33m===\033[m'*15, 'EX039', '\033[33m===\033[m'*15)
nascimento = int(input('Digite seu ano de nasciemnto: '))
atual = date.today().year
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('Você tem {} anos e está na hora de se alistar!'.format(idade))
elif idade < 18:
    falta = 18 -idade
    alistamento = atual + falta
    print('Você tem {} anos e falta {} para se alistar!'.format(idade, falta))
    print('Você deverá se alistar em {}'.format(alistamento))
else:
    passou = idade - 18
    alistamento = atual - passou
    print('Você tem {} anos e passou {} da idade para se alistar!'.format(idade, passou))
    print('Você deveria ter se alistado em {}'.format(alistamento))
