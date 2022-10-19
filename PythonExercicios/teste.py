lista = [5,3,1,4,2]

tamanho = len(lista)
maior = menor = lista[0]
for i in range(0, tamanho):
    if lista[i + 1] < lista[i]:
        aux = lista[i + 1]
        lista[i + 1] = lista[i]
        lista[i] = aux


print(lista)