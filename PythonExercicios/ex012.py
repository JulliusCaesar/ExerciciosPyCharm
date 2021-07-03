print('===== ex012 =====')
p = float(input('Digite o Preço: '))
# d = p *0.05
# pd = p - d
pd = p - (p * 5 / 100)
print('O valor do produto é R$ {:.2f} e com desconto de 5% fica R$ {:.2f}'.format(p, pd))
