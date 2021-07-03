'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: A média de idade
do grupo, qual é o nome do homem mais velho, quantas mulheres tem menos de 20 anos'''
print('===='*10, ' EX056 ', '===='*10)
v = 0
m = 0
media = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo F /M? ')).upper().strip()
    media += idade
    if sexo == 'M' and c == 1:
        nome2 = nome
        v = idade
    if sexo == 'M':
        if idade > v:
            nome2 = nome
            v = idade
    else:
        if idade < 20:
            m = m + 1
print('O Homem mais velho é {} e tem {} anos. '.format(nome2, v))
print('Tem {} Mulheres com menos de 20 anos.'.format(m))
print('A média de idade das pessoas é de {} anos!'.format(media/4))
