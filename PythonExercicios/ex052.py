'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo'''
print('===='*10, ' EX052 ', '===='*10)
primo = int(input('Digite o Número para descobrir se ele é ou não PRIMO: '))
tot = 0
for c in range(1, primo + 1):
    if primo % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[33m', end=' ')
    print('{} '.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes '.format(primo, tot))
if tot == 2:
    print('E por isso ele é Primo!')
else:
    print('E por isso ele não é Primo!')
