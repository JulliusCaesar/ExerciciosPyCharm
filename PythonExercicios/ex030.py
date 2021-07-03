'''Crie um programa que leia um número inteiro e mostre se ele é Par ou Impar.'''
print('====='*10, 'EX030', '====='*10)
inteiro = int(input('Digite um número inteiro: '))
pi = inteiro % 2
if pi == 0:
    print('Esse número é PAR')
else:
    print('Esse número é IMPAR')
