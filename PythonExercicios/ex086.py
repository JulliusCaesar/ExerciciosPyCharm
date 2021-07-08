'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com os valore lidos pelo teclado. No final,
mostre a matriz na tela, com a formatação correta.'''
matriz = [[], [], []]
c = c2 = c3 = 0
for c in range(0, 9):
    matriz[c2].append(int(input(f'Digite um valor para [{c2}][{c3}]: ')))
    c3 += 1
    if c3 == 3:
        c2 += 1
        c3 = 0
for p in matriz:
    print(f'[  {p[0]} ] [  {p[1]} ] [  {p[2]} ]')
