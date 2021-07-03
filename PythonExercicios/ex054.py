'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores'''
print('===='*10, ' EX054 ', '===='*10)
from datetime import date
atual = date.today().year
p = 0
p2 = 0
for c in range(1, 8):
    data = int(input("Digite o ano de nascimento da {}º pessoa: ".format(c)))
    m = atual - data
    if m < 21:
        p += 1
    else:
        p2 += 1

print('Tem {} que não completaram a Maioridade!'.format(p))
print('Tem {} que já compeltaram a Maioridade!!'.format(p2))
