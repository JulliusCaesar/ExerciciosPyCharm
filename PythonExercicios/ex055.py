'''Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos'''
print('===='*10, ' EX055 ', '===='*10)
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o Peso da {}º pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O Maior peso é {}kg e o menor é {}kg'.format(maior, menor))
