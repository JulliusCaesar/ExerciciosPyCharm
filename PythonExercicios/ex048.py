'''Faça um programa que calcule a soma entre todos os números impares que são multiplos de tres e que se encontram
no intervalo de 1 até 500'''
print('====='*8, 'EX048', '====='*8)
s = 0
cont = 0
for c in range(1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            s += c
            cont += 1
print('A Soma entre todos os {} números impares divisiveis por 3 é {}.'.format(cont, s))

# for c in range(1, 501, 2):
#   if c % 3 == 0:
#       s = s + c
