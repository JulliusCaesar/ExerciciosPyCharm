"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se uma pessoa tem voto, NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições."""
from datetime import datetime


def voto(ano_nascimento):
    idade = datetime.now().year - ano_nascimento
    global ano_usuario
    if idade < 18:
        ano_usuario = idade
        return "NÃO VOTA."
    elif idade < 65:
        ano_usuario = idade
        return 'VOTO OBRIGATÓRIO.'
    else:
        ano_usuario = idade
        return "VOTO OPCIONAL."


print('---' * 10)
ano_usuario = int(input('Em que ano você nasceu? '))
idade_voto = voto(ano_usuario)
print(f'Com {ano_usuario} anos: {idade_voto}')
