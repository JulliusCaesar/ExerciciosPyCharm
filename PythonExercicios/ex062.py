'''Melhore o desafio 061, perguntando para o usúario se ele quer mostrar mais alguns termos, O programa encerra
quando ele disseer que quer mostrar 0 termos'''
print('{:=^80}'.format('EX062'))

termo = int(input('Digite o Primeiro termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{}'.format(termo), end=' -> ')
        c += 1
        termo = termo + razao
    print('PAUSA')
    mais = int(input('Quantos termos você quer ver a mais? '))
print('FIM')
print('Progrssão finalizada com {} termos mostrados.'.format(total))
