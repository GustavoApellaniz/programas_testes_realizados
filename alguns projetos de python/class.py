i = 0
total = 0
class negative_number(Exception):
    pass
    
n = int(input("coloque o numero que vc quer ter para somar mais numeros, fez sentido, não né? "))
while i<n:
    try:
        y = int(input())
        i+= 1
        if y<0:
            raise negative_number
        total += y
    except negative_number:
        print('numero negativo') 

print(f'{total}')

