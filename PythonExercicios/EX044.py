'''Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento
- A vista dinheiro/cheque 10% de desconto. - a vista no cartão 5% de desconto. - em até 2x no cartão preço normal.
- 3x ou mais 20% de juros'''
print('===='*9, 'EX044', '===='*9)
print('{:=^80}'.format(' LOJAS JC SILVA '))
produto = float(input('Preço da compra: R$'))
op = int(input('''Forma de Pagamento  
Op 1 = a Vista  
Op 2 = Cartão 
Op 3 = 2x sem juros 
Op 4 = 3x ou mais com juros 
 Escolha uma opção: '''))

if op == 1:
    desproduto = produto - (produto * 0.1)  # produto - ( produto * 10 / 100)
    print('Á vista você tem 10% de desconto.\n Você pagará R$ {:.2f}'.format(desproduto))
elif op == 2:
    desproduto = produto - (produto * 0.05)  # produto - ( produto * 5 / 100)
    print('No Cartão em 1x você tem 5% de desconto.\n Você pagará R$ {:.2f}'.format(desproduto))
elif op == 3:
    parcela = produto / 2
    print('Parcelado ficará em 2 vezes de R$ {:.2f}'.format(parcela))
elif op == 4:
    totparcela = int(input('Quantas parcelas: '))
    des = produto * 0.2
    desproduto = produto + des
    parcela = desproduto / totparcela
    print('Parcelado ficará no valor de R$ {:.2f} dividido em {} vezes de R$ {:.2f}'.format(desproduto, totparcela, parcela))
else:
    print('\033[32mOPÇÃO ERRADA\033[M')