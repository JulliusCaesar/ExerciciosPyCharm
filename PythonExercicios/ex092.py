'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre os (com idade) em um dicionário
se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule
e acrescente além da idade, com quantos anos a pessoas vai se aposentar.'''
from datetime import date
carteiraTrabalho = dict()

while True:
    carteiraTrabalho['nome'] = str(input("Nome: "))
    anoAtual = date.today().year
    anoNascimento = int(input('Ano de Nascimento: '))
    carteiraTrabalho['idade'] = anoAtual - anoNascimento
    carteiraTrabalho['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    if carteiraTrabalho['ctps'] == 0:
        break
    carteiraTrabalho['contratação'] = int(input('Ano de Contratação: '))
    idadeContratacao = carteiraTrabalho['contratação'] - anoNascimento
    carteiraTrabalho['aposentadoria'] = idadeContratacao + 35
    carteiraTrabalho['salário'] = float(input('Salário: '))
    break
print('-=' * 40)
for Key, Value in carteiraTrabalho.items():
    print(f'{Key} tem o valor {Value}')
