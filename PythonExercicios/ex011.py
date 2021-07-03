larg = float(input('Largura da Parede: '))
alt = float(input('Altura da Parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar sua parede você precisará de {}L de tinta.'.format(tinta))
