'''Refaça o exercicio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado;
- Equilátero todos os lados iguais. - Isóceles dois lados iguais. Escaleno todos os lados diferentes.'''
print('====='*15, 'EX042', '====='*15)
print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmento acima \033[34mPODEM FORMAR\033[m triângulo ', end='')
    if r1 == r2 and r1 == r3:  # Python aceitaria se fosse escrito r1 == r2 == r3
        print('\033[31mEQUILÁTERO\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[32mESCALENO.\033[m')
    else:
        print('\033[33mISÓCELES.\033[m')
else:
    print('Os segmentos acima \033[36mNÃO PODEM FORMAR\033[m triângulo')
