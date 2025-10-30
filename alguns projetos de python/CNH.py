x = int(input("qual sua idade? "))
if(x>=18):
    print("você tem idade para dirigir")
    x = True
else:
    print("você não tem a idade necessária")

y = str(input("você possui CNH? "))

if(y == 'sim'):
    y = True

if(x == True and y == True ):
    print("você pode dirigir")
elif(x == True and y == False):
    print('você precisa da CNH')
elif(x == False and y == True):
    print('você não tem idade para dirigir mas tem cnh?')
else:
    print('você não possui nenhum dos requisitos para drigir')