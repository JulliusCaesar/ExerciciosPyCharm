'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou não continuar.
No final mostre a) quantas pessaos tem mais de 18 anos. b) quantos homens foram cadastrados. c) quantas mulheres tem
menso de 20 anos'''
maior = cm = cf = 0
while True:
    print('---'*20)
    print('CADASTRE UMA PESSOA')
    print('---'*20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    while sexo not in 'mMfF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        cm += 1
    if sexo == 'F' and idade < 20:
        cf += 1
    print('---'*20)
    resp = str(input('Quer Continuar [S/N]: ')).strip().upper()[0]
    while resp not in 'SsNn':
        resp = str(input('Quer Continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('==== FIM DO PROGRAMA ====')
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {cm} Homens cadastrados')
print(f'E temos {cf} mulheres com menos de 20 anos')

