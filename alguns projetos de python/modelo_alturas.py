menor = 0
maior = 0
media = 0
soma_altu = 0
lista_menores = []

for i in range(3):
    x = float(input())
    if x> maior:
        maior = x
    if x< 160/100:
        menor += 1
        lista_menores.append(x)

    soma_altu += x

print('aqui estão os numeros')
print(f"{soma_altu/3:.2f}")
print(maior)
print(lista_menores)
print(menor)

    
    
