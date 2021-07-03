import random

print('===== EX020 =====')
n1 = str(input('Digite o nome do 1º Aluno: '))
n2 = str(input('Digite o nome do 2º Aluno: '))
n3 = str(input('Digite o nome DO 3º Aluno: '))
n4 = str(input('Digite o nome do 4º Aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de execução é: ')
print(lista)
