from math import sin, cos, tan, radians
print ('===== EX018 =====')
angulo = float(input('Digite o Ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O Ângulo {} tem o SENO de {:.2f} o COSSENO de {:.2f} e a TANGENTE de {:.2f} '.format(angulo, seno, cosseno, tangente))
