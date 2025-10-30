from random import randint

#def par_impar(x):
#   if x %2 == 0

if __name__ == '__main__': 
    a = randint(0, 100000)
    print("vamos jogar par ou impar")
    x = input()
    if x != 's':
        print("jogo encerrado")
    else:
        print("ótimo")
        print("escolha um número")
        y=int(input())
        print('par ou ímpar? ')
        z=input("P/I ")
        if z == 'P':
            for l in range(a,a+1):
                if (l + y)%2 == 0:
                    print(f"o meu número foi {l}")
                    print("you won")
                    break
                else:
                    print(f"o meu número foi {l}")
                    print('you lose')
                    break

        elif z == 'I':
             for l in range(a,a+1):
                if (l + y)%2 == 0:
                    print(f"o meu número foi {l}")
                    print("you lose")
                    break
                else:
                    print(f"o meu número foi {l}")
                    print('you win')
                    break

        

