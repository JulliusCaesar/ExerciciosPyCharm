''' import math
print('===== EX016 =====')
real = float(input('Digite um número Real qualquer: '))
print('O número {} te a parte inteira {}.'.format(real, math.floor(real)))'''
# math.trunc() seria o melhor pois ele realmente pega a parte inteira do número
# poderia tbm ter somente chamado o metodo trunc usando o FROM IMPORT MATH TRUNC
num = float(input('Digite o valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
