'''Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os
em uma lista, já na posição correta de inserção(sem usar o sort()). No final, mostre a lista
ordenada na tela.'''
lista = list()
num = int(input('Digite um valor: '))
if num > 5:
    print('Valor adicionado no final do lista!')
    lista.insert(5, num)
else:
    print('Valor adicionado no começo da lista!')
for c in range(0, 4):
    valor = int(input('Digite um valor: '))
    if valor > num:
        lista.insert(5, valor)
        print('Valor adicionado no final do lista!')
    else:
        lista.insert(0, valor)
        print('Valor adicionado no começo da lista!')
print(lista)
