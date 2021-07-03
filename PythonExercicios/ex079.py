'''Crie um programa aonde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o númerero
já exista la dentro ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
crescente'''
lista = list()
lista.append(int(input('Digite um valor: ')))
print('Valor Adicionado com sucesso...')
while True:
    resp = str(input('Gostaria de continuar [S/N]: ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Gostaria de continuar [S/N]: ')).strip().upper()
    if resp == 'N':
        break
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        print('Valor Adicionado com sucesso...')
        lista.append(valor)
    else:
        print('Valor Duplicado! Não vou adicionar...')
print('-=' * 40)
print(f'Você digitou os valores {lista}')
