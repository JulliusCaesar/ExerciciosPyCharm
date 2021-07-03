'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares, Se o valor
digitado for IMPAR, desconsidere-o'''
print('===='*10, ' EX050 ', '===='*10)
soma = 0
for c in range(1, 7):
    par = int(input('Digite o {}º valor inteiro: '.format(c)))
    if par % 2 == 0:
        soma += par
print('A soma dos números pares é {}'.format(soma))
