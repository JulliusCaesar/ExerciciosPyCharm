'''Faça um programa que leia 3 números e mostre qual é o Maior e o Menor '''
print('===== EX033 =====')
maior = 0
menor = 0
a = int(input('Digite o primeiro Valor: '))
b = int(input('Digite o Segundo valor: '))
c = int(input('Digite o Terceiro valor: '))
# verificando que é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o MAIOR
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O número Maior é {} e o número Menor é {}'.format(maior, menor))