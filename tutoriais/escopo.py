#visibilidade da variavel
#escopo local e global


x = 'esquece'


def y():
    x = 'lembre'
    print(x)



if __name__ == '__main__':
    y()
    print(x)