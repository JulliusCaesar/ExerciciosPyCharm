def ficha(jog='<Desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols no campeonato.')


# Programa Principal

nome = str(input("Nome do Jogador: "))
gols = str(input("Número de Gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == "":
    ficha(gol=gols)
else:
    ficha(nome, gols)
