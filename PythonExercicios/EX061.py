'''Refaça o o Desafio 051, lendo o primeiro termo e a razão de uma PA. mostrando os 10 primeiros termos da progrssão
usando a estrutura while'''
print('{:=^80}'.format('EX060'))

termo = int(input('Digite o Primeiro termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
c = 1
while c <= 10:
    print('{}'.format(termo), end=' -> ')

    c += 1
    termo = termo + razao
print('Fim')
