'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
continuar. No final, mostre: a) Qual é o total gasto na compra. b) quantos produtos custam mais de 1000. c) qual é o
nome do produto mais barato.'''
print('---'*15)
print('{:.^40}'.format('LOJA SUPER BARATÃO'))
print('---'*15)
menor = total = tprod = 0
produtom = ''
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))
    cont = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if menor == 0 or preco < menor:
        menor = preco
        produtom = produto

    if preco >= 1000:
        tprod += 1
    total += preco
    if cont == 'N':
        break
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {tprod} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {produtom} que custa R$ {menor}')