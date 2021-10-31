"""Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opicionais: o nome de um jogador
e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não
tenha sido informado corretamente."""


def ficha():
    nome_jogador = str(input("Nome do Jogador: "))
    if nome_jogador == '':
        nome_jogador = '<Desconhecido>'
    quant_gols = str(input("Número de Gols: "))
    if quant_gols == '':
        quant_gols = int(0)
    print(f'O Jogador {nome_jogador} fez {quant_gols} gol(s) no campeonato.')


ficha()
