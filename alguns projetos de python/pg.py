from math import sqrt
a1 = int(input('primeiro numero'))
n = int(input('numero de vezes'))
q = int(input('razao'))
i = 0
total = 0

while i<q:
    total = total * q
    print(total)
    i+= 1




ultimo_termo = a1 * q**(n - 1)
soma = a1 * ((q**n - 1) / (q - 1))

print(f'soma dos resultados {soma}')
print(ultimo_termo)