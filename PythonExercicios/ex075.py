'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
a) Quantas vezes apareceu o valor 9. b) Em que posição foi digitado o primeiro valor 3. c) Quais foram os números pares
'''
digitados = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
             int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores {digitados}')
print(f'O valor 9 apareceu {digitados.count(9)} vezes.')
print('O valor 3 não aparece em nenhuma posição' if 3 not in digitados
      else f'O valor 3 apareceu na {digitados.index(3)+1}ª posição')
print('O valores pares digitados foram ', end='')
for c in range(0, len(digitados)): # for c in digitados: tbm serviria
    if digitados[c] % 2 == 0:
        print(f'{digitados[c]}', end=' ')
print('\n Fim do programa!')
