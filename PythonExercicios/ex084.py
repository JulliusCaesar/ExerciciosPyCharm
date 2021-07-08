'''Faça um programa que leia nme e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas. b) Uma listagem com as pessoas mais pesadas. c) Uma listagem com as pessoas
mais leves'''
NomePeso = list()
final = list()
maior = menor = 0
while True:
    NomePeso.append(str(input('Nome: ')))
    NomePeso.append(float(input('Peso: ')))
    if len(final) == 0:
        maior = menor = NomePeso[1]
    else:
        if NomePeso[1] > maior:
            maior = NomePeso[1]
        if NomePeso[1] < menor:
            menor = NomePeso[1]
    final.append(NomePeso[:])
    NomePeso.clear()
    resp = str(input('Gostaria de continuar [S/N]: ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Gostaria de continuar [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('-='*30)
print(f'Ao todo você cadastrou {len(final)} pessoas.')
print(f'O maior Peso foi de {maior}Kg. Peso de ', end='')
for p in final:
    if p[1] == maior:
        print(f'[{p[0]}] ', end="")

print()
print(f'O menor Peso foi de {menor}Kg. Peso de ', end='')
for p in final:
    if p[1] == menor:
        print(f'[{p[0]}] ', end="")
