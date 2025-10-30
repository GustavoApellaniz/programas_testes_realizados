
#a cada 2 m2 de parede se precisa 1l de tinta

def area(b,a):
    return a*b




if __name__ == '__main__':
    x = float(input('qual a largura da sua parede '))
    y = float(input('qual a altura  da sua parede '))
    print(f'altura: {y}\n largura: {x}\n logo fica {y}x{x} e sua área é {area(x,y)}')
    z = (area(x,y))/2
    print(f"você precisaria para pintar a parede de {round(z,2)}l de tinta")

