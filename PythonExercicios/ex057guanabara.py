sexo = str(input('Informe seu sexo: [F/M] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor Informe seu sexo: [F/M] ')).strip().upper()[0]
print('Sexo {} registrado com Sucesso '.format(sexo))
