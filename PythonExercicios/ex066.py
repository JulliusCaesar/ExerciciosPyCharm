'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usúario digitar
o valor 999, que é a condição de parada. No final , mostre quantos números foram digitados, e qual foi a soma entre
eles (desconsiderando o flag)'''
soma = quant = num = 0
while True:
    num = int(input('Digite um valor Inteiro (999 para parar): '))
    if num == 999:
        break
    soma += num
    quant += 1
print(f'Você digitou {quant} números e a soma entre eles foi {soma}')
