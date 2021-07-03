'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os n primeiros elementos de uma
sequencia de fibonacci. EX: 0 1 1 2 3 5 8'''
print('{:=^80}'.format('EX062'))
f = int(input('Quantos termos você quer mostrar: : '))
ant = 0
prox = 0
fibo = 1
while f >= 0:
    if ant == 0:
        print(' {} -> '.format(ant), end=' 1 -> ')
    prox = ant + fibo
    print(' {} '.format(prox), end=' -> ')
    ant = fibo
    fibo = prox
    f -= 1

