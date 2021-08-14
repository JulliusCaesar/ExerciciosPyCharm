''' Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre
uma mensagem com tamanho adaptável. Ex: escreva('Olá Mundo') '''


def escreva(entrada):
    tam = len(entrada) + 6
    print(f'{"~"}' * tam)
    print(f'{entrada:^10}')
    print(f'{"~"}' * tam)


escreva('Curso em')

escreva('julio')

escreva('CeV')
