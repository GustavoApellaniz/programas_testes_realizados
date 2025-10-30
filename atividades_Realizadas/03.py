class negativeerror(Exception):
    pass

def negativo(a):
    if a<0:
        raise negativeerror
    return (a*0.95)


if __name__ == '__main__':
    while True:
        try:
         x = float(input("numero da compra? "))
         negativo(x)
        except negativeerror:
            print('numero negativo é inválido')
            break
        print(f'esse é o valor original {x} \n com o 5% de desconto ele fica {negativo(x)}')
        break
            

    
