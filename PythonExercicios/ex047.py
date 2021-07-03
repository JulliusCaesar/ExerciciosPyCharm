'''Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 e 50'''
print('====='*8, 'EX047', '====='*8)
print('=-'*8, ' Números Pares entre 1 e 50 ', '=-'*8)
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
print(' Acabou!')

# for c in range(2, 51, 2):
#  print(c, end=' ')
# com esses comandos posso diminuir o trabalho do processador
