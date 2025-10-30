#Use reduce para somar todos os elementos da lista [5, 10, 15, 20].

from functools import reduce
lista = [5, 10, 15, 20]

def soma(x):
    return x%2 != 0

y = list(filter(soma,lista))
print(y)

map
filter 
reduce
