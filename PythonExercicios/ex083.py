'''Crie um programa onde o usuário digite uma expressão qualquer que use parenteses. Seu aplicativo deverá
analisar se a expressão passada está com os parenteses abertos e fechado na ordem correta'''

lista = (str(input('Digite a expressão: ')))
p1 = lista.count('(')
p2 = lista.count(')')
if p1 == p2:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está errada!')
