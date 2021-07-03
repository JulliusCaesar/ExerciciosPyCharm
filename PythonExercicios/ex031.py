'''Desenvolva um progrma que pergunte a distância de uam viagem em Km. Calcule o preço da passagem, cobrando
0.50 centavos por Km para viagens de até 200km e 0.45 centavo para viagens mais longas'''
print('===== EX031 =====')
viagem = float(input('Qual a distância da sua viagem em KM? '))
'''if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.4'''
preco = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print('Você esá prestes a fazer uma viagem de {:.2f}km e o valor da sua passagem é de R${:.2f}'.format(viagem, preco))
