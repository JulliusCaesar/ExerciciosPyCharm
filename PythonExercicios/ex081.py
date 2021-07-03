'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
a) Quantos números foram digitados. b) A lista de valores, ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista.'''
lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Gostaria de continuar [S/N]: ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Gostaria de continuar [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('-='*40)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista e aparece {lista.count(5)} vezes')
else:
    print('O valor 5 não foi encontrado na lista!')
