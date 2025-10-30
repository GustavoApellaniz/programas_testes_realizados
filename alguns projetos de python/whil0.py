listadiv = []
y = 1
total = 0

while y != 0:
    y = int(input('escreva um n '))
    if y%2 == 0 or y%3 == 0:
        listadiv.append(y)
    total += 1
print(f'o total de numeros foi {total}, e os n div por 2 e 3 são {listadiv}')