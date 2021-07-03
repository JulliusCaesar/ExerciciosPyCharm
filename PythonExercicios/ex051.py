'''Desenvolva um programa que leia o primeiro termo e a razão de uam PA. No final, mostre os 10 primeiros termos
dessa progressão'''
print('===='*10, ' EX051 ', '===='*10)
termo = int(input('Digite o Primeiro termo da PA: '))
razao = int(input('Digite a Razão da PA: '))

for c in range(1, 11):
    print('O {}º Termo é: {}'.format(c, termo))
    termo = termo + razao

