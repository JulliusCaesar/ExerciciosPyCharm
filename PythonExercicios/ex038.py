'''Escreva um programa que leia dois números inteiros e compare-os, mostrando uma mensagem na tela
 - o primeiro valor é maior. - o segundo valor é maior. - não existe valor maior, os dois são iguais'''
print('\033[33m===\033[m'*15, 'EX038', '\033[33m===\033[m'*15)

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 > num2:
    print('O Primeiro número é Maior.')
elif num2 > num1:
    print('O Segundo número é Maior')
else:
    print('Não existe valor maior, os dois são iguais.')
