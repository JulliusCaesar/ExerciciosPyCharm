'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores impares digitads, respectivamente. Ao final
mostre o conteúdo das três listas geradas'''
lista = list()
lista1 = list()
lista2 = list()
c = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Gostaria de continuar [S/N]: ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Gostaria de continuar [S/N]: ')).strip().upper()
    if resp == 'N':
        break
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        lista1.append(lista[c])
    else:
        lista2.append(lista[c])
print('-='*40)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista1}')
print(f'A lista de impares é {lista2}')
