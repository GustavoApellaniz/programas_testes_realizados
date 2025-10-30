lista = []
n = int(input())
for i in range(n+1):
    if n<=100:
        print('precisa ser maior que 100')
        break
    else:
         if i%2 == 0:
            lista.append(i)

print(lista)
