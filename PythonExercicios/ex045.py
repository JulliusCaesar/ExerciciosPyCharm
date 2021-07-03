'''Crie um programa que faça o computador jogar jokempo com voce'''
import random
from time import sleep
print('====='*15, 'EX045', '====='*15)
print('Vamos jogar Joken Po!!')
pjoken = random.randint(1, 3)

joken = int(input(' \n 1 = Pedra\n 2 = Papel \n 3 = Tesoura\n Digite: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('=-='*10)
if joken == 1 and pjoken == 2:
    print('Você jogou  Pedra \nComputador jogou Papel! Você Perdeu!!')
elif joken == 2 and pjoken == 3:
    print('Você jogou Papel \nComputador jogou Tesoura! Você Perdeu!!')
elif joken == 3 and pjoken == 1:
    print('Você jogou Tesoura \nComputador jogou Pedra! Você Perdeu!!')
elif joken == 1 and pjoken == 3:
    print('Você jogou Pedra \nComputador jogou Tesoura! Você Venceu!!')
elif joken == 2 and pjoken == 1:
    print('Você jogou Papel \nComputador jogou Pedra! Você Ganhou!!')
elif joken == 3 and pjoken == 2:
    print('Você jogou Tesoura \nComputador jogou Papel! Você Ganhou!!')
else:
    print('Deu Empate')
print('=-='*10)