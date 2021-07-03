print('===== EX013 =====')
salario = float(input('Digite o Salário do Funcionário: '))
# aumento = salario * 0.15
# nsalario = salario + aumento
nsalario = salario + (salario * 15 / 100)
print('O funcionário teve aumento de 15% passando a receber R$ {:.2f}'.format(nsalario))
