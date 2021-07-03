print('===== EX022 =====')
nome = str(input('Digite o seu Nome Completo: ')).strip()
print(nome.upper())
print(nome.lower())
# div = nome.split()
# div1 = div[0]
# nome = nome.replace(' ', '')
print('Seu nome tem {} caracteres sem contar os espaços.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
