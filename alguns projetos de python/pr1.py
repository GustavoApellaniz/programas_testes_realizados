x = {'azul','vermelho','amarelo','verde'}
y = {'azul','vermelho','amarelo','verde','roxo','ciano'}

print( x | y)
print(x.union(y))

print(x & y)
print(x.intersection(y))

print( x ^ y)
print(x.symmetric_difference(y))

x.add("só adicionar um elemento")
x.remove("azul")
x.discard('vermelho')
x.pop() # elemina um elemento aleatório  


