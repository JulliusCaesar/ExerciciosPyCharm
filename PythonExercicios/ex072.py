'''Crie um programa que tenha TUPLA totalmente preenchida com uam contagem por extenso. de zero a vinte
Seu programa deverá ler um número pelo teclado (entre 0 até 20) e mostrá-lo por extenso'''
numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    cont = int(input('Digite um número de 0 a 20: '))
    while cont < 0 or cont > 20:
        cont = int(input('Tente Novamente. Digite um número de 0 a 20: '))
    print(f'Você digitou o número {numero[cont]}')
    resp = str(input('Gostaria de continuar [S/N]: ')).strip().upper()
    if resp not in 'SN':
        resp = str(input('Gostaria de continuar [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('Fim do programa.')
# if 0 <= cont <= 20:
#   break poderia ter sido usado para a entrada de dados na laço while
