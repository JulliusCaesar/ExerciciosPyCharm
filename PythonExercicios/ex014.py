print('====== EX014 =====')
c = float(input('Informe a Temperatura em ºC: '))
f = ((9 * c) / 5) + 32 # aqui a ordem de precedência não necessita de parenteses
print('A temperatura de {}ºC corresponde a {}ºF! '.format(c, f))
