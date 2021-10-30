"""Crie um programa que tenha a função fatorial() que receba dois parãmetros: o primeiro que indique o número a calcular
e o outro chamado show, que será um valor logico(opcional) indicando se será mostrando ou não na tela o processo
de cálculo do fatorial"""


def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    if show:
        fator = 1
        print('---' * 10)
        for c in range(num, 0, -1):
            print(f'{c} x ', end='')
            fator *= c
        print(end='= ')
        return fator
    else:
        fator = 1
        print('---' * 10)
        for c in range(num, 0, -1):
            fator *= c
        return fator


print(fatorial(5))
