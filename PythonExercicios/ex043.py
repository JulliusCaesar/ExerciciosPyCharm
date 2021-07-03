'''Desenvolva uma logica que leia o peso e a altura de uma pessoa. Calcule o IMC e mostre seu status, de acordo com a tabla abaixo
- Abaixo de 18,5 ABAIXO DO PESO. - Entre 18,5 e 25 PESO IDEAL. - 25 até 30 SOBREPESO. - 30 até 40 OBESIDADE - Acima de 40 OBESIDADE
MÓRBIDA'''
print('====='*15, 'EX043', '====='*15)

peso = float(input('Digite seu PESO: '))
altura = float(input('Digite sua ALTURA: '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está com OBSEIDADE!')
else:
    print('Você está com OBSEDAIDE MORBIDA!')
