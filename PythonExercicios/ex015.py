print('===== EX015 =====')
dias = int(input('Quantos dias o carro foi alugado?' ))
km = float(input('Quantos Kilometros foi percorrido? '))
tdias = (dias * 60) +(km * 0.15)
# tkm = km * 0.15
print('Você pagara R${:.2f} pelo aluguel do carro!'.format(tdias))
