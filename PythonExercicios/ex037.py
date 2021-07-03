'''Escreva um programa que leia um numéro inteiro qualquer e peça para o usuário escolher qual será a base
de conversão: 1 para Binário 2 para Octal e 3 para Hexadecimal'''

print('\033[33m===\033[m'*15, 'EX037', '\033[33m===\033[m'*15)

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para Hexadecimal''')
op = int(input('Sua opção: '))

if op == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida.')

