'''Faça um programa que leia um número qualqueer e mostre o seu fatorial. EX: 5 = 5 X 4 X 3 X 2 X 1 = 120'''
'''print('{:=^80}'.format('EX060'))
cont = int(input('Escolha o número para realizar o fatorial: '))
cont2 = cont - 1
div = cont
while cont2 != 0:
    div *= cont2
    cont2 -= 1
print('O fatorial de {} é {}'.format(cont, div))'''

'''from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O Fatorial de {} é {}. '.format(n, f))'''

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('{}. '.format(f))

