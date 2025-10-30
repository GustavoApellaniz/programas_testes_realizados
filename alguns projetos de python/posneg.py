x = int(input())
i = 0
total = 0
neg = 0
while i<x:
    y = int(input())
    if y> 0:
        total += y
    else:
        neg += y
    i+=1
print(f'soma positivo {total}')
print(f'soma negativo {neg}')