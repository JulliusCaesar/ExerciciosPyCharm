'''Escreva um programa para aprovar o emprestimo bancário para compra de uma casa. O programa vai perguntar
o valor da casa, o salário do comprador e em quantas anos ele vai pagar. Calcule o valor da prestação mensal,
sabendo que ela não pode exceder o valor de 30% do salário ou então o empréstimo será negado'''

print('\033[33m===\033[m'*15, 'EX036', '\033[33m===\033[m'*15)
print('\033[37mResponda as pergauntas para saber se o Empréstimo será aprovado.\033[m')
casa = float(input('Qual o valor da Casa que irá comprar? '))
salario = float(input('Qual o seu Salário atual? '))
anos = int(input('Em quantos anos irá pagar? '))
nparcelas = anos * 12  # pderia ter feito parcela = casa / (anos * 12)
parcela = casa / nparcelas
porcento = salario * 0.3  # poderia tbm ter feito porcento = salario * 30 /100

if parcela > porcento:
    print('A parcela de R${:.2f} excede os 30% do seu Salário de R${:.2f}, então o empréstimo foi negado.'.format(parcela, salario))
else:
    print('Parabés você comprou a casa no valor de R${:.2f}, suas parcelas serão em {}x de R${:.2f}'.format(casa, nparcelas, parcela))
