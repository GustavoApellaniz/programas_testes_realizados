#Dada a lista [10, 15, 20, 25, 30], use filter para selecionar apenas os números múltiplos de 10.
lista = [10, 15, 20, 25, 30]

def mult(x):
    return x%10 == 0

y = list(filter(mult, lista))
print(y)