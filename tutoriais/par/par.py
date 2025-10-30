from random import randint

def jogo(x,y):
    if (x % 2 == 0 and y.upper() == 'P') or (x % 2 != 0 and y == 'I'):
            print("Você ganhou!")
            print(f'meu numero foi {l}, e a soma foi {x}')
            return 0
    else:
            print("Você perdeu!")
            print(f'meu numero foi {l}, e a soma foi {x}')
            return 1

l = randint(0,10)
print("numero")
y = int(input())
z = input("P/I ")
soma = l+y
print(jogo(soma,z))
