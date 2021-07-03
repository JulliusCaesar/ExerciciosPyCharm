'''Crie um programa que tenha uma tupla única com nomes de produtos e seu respectivos preços, na sequencia.
No final, mostre uma listagem de peços, organizando os ddos em forma tabular'''
listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*50)
print('{:^50}'.format('LISTAGEM DE PREÇOS')) # print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*50)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<40}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*50)
