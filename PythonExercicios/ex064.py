''' Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
 valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag) '''
print('{:=^80}'.format('EX064'))
n = c = soma = 0
print('Para parar o programa digite 999.')
n = int(input('\nDigite um valor Inteiro: '))
while n != 999:
    c += 1
    soma += n
    n = int(input('\nDigite um valor Inteiro: '))
print('Fim do programa. Você digitou {} números. e a soma deles é {}'.format(c, soma))
''' if n == 999:
        print('Fim do programa. Você digitou {} números. e a soma deles é {}'.format(c - 1, soma))
    else:
        soma += n'''
