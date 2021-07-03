'''Crie um programa que leia dois valores e mostre um menu na tela, [1] Somar [2] multiplicar [3] maior [4] novos números
[5] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.'''
print('{:=^80}'.format('EX059'))
op = 0
while op != 5:
    n1 = float(input('Digite um valor: '))
    n2 = float(input('Digite outro valor: '))
    op = int(input('''
    Digite o que quer fazer:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Digitar novos números
    [ 5 ] Sair do programa 
    '''))
    if op == 1:
        soma = n1 + n2
        print('{:.1f} + {:.1f} = {:.1f} '.format(n1, n2, soma))
    elif op == 2:
        mult = n1 * n2
        print(' {} x {} = {} '.format(n1, n2, mult))
    elif op == 3:
        if  n1 > n2:
            print('O maior valor é {}'.format(n1))
        elif n2 > n1:
            print('O maior valor é {}'.format(n2))
        else:
            print('Não existe Maior valor.')
