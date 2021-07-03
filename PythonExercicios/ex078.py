'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, o maior e o menor valor digitado
e as suas respecitivas posições na lista'''
lista = list()
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}:  ')))
    if c == 0:
        maior = menor = lista[0]
    if lista[c] > maior:
        maior = lista[c]
    if lista[c] < menor:
        menor = lista[c]
print('-='*30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for c in range(0, 5):  # for i, v in enumerate(lista)
    if maior == lista[c]:  # if v == maior:
        print(f'{c}... ', end='')  # print(f'{i}...')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for c in range(0, 5):
    if menor == lista[c]:
        print(f'{c}... ', end='')
