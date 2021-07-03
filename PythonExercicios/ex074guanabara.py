from random import randint
aleatorio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in aleatorio:
    print(f'{n} ', end="")
print(f'\nO maior valor sorteado foi {max(aleatorio)}')
print(f'O menor valor sorteado foi {min(aleatorio)}')
