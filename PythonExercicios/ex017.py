import math
# from math import pow, sqrt
co = float(input('Entre com o valor do cateto oposto: '))
ca = float(input('Entre com o valor do cateto adjacente: '))

# hipotenusa = sqrt((pow(ca, 2) + pow(co,2)))
hi = math.hypot(co, ca)
print("\n**************************\n")

print("O valor da hipotenusa é: {:.2f}".format(hi))
