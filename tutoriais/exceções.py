
def quq(a):
    if a == 1 or a == 0:
       return 1
    else:
       return a * quq(a-1)




if __name__ == '__main__':
   try:
     print("escolha um número ")
     x = int(input())
   except RecursionError:
       print('número muito alto ou negativo')
   print(quq(x))