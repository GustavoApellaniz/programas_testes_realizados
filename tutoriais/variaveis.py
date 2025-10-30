x = float(input("primeira nota"))
y = float(input("segunda nota"))

z =(x+y)/2
if(z>7):
    print("aprovado")
    
elif(z>5):
    print("recupreação")
else:
    print("reprovado")

print(f"sua nota foi \'{z:.4f}\'4")


num = 1
while(num<=10):
    print(num)
    num = num+1
    