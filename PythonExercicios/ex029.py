''' Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem
dizendo que ele foi multado. A multa vai custar 7 reais por cada km acima do limite'''
print('=====' * 10, 'EX029', '=====' * 10)
velocidade = float(input('Qual a velocidade do Carro: '))
if velocidade > 80:
    acima = velocidade - 80
    multa = acima * 7
    print('O carro passou {:.2f}kmh/h acima da velocidade e pagará R${:.2f} de multa.'.format(acima, multa))
else:
    print('O carro está dentro da velocidade permitida andando a {:.2f}km/h.'.format(velocidade))
