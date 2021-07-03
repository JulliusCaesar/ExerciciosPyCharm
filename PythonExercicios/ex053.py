'''Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços'''
print('===='*10, ' EX053 ', '===='*10)
frase = str(input('Digite uma frase e verificaremos se elá é um PALINDROMO: ')).strip()
frase = frase.replace(' ', '')
controle = len(frase)
teste = 0
for c in range(0, controle):
    if frase[c] == frase[controle - 1]:
       # print('{}  {}'.format(frase[c], frase[controle - 1]))
        teste = teste + 1
    controle = controle - 1
if teste == len(frase):
    print('É uma frase PALINDROMO!!')
else:
    print('Não é uma frase PALINDROMO!!!')