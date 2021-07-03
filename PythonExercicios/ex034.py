'''Escreva um programa que pergunte o salario de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$ 1.250,00, calcule um aumento de 10%. Para inferiores ou iguais o aumento é de 15%'''
print('===== EX034 =====')
sal = float(input('Digite o salário do Fncionário: '))
if sal <= 1250:
    aumento = sal + (sal * 15/100)

else:
    aumento = sal + (sal * 10/100)

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} '.format(sal, aumento))
