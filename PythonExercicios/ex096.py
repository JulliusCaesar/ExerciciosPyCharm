"""Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a aréa do terreno"""


def area(largura, comprimento):
    área = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {área}m²')


# programa principal
print('Controle de Terrenos')
print('---------------------')
larguraTerreno = float(input('LARGURA (m): '))
comprimentoTerreno = float(input('Comprimento (m): '))
area(larguraTerreno, comprimentoTerreno)
