print('===== EX027 =====')
nome = str(input('Digite seu nome completo: ')).strip()
print('Prazer em te conhecer!!')
nome1 = nome.split()

print('Seu nome completo é {} \n '
      'Seu primeiro nome é {} \n'
      ' seu último nome é {}'.format(nome, nome1[0], nome1[len(nome1) - 1]))

