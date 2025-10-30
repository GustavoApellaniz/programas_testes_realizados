#considerações finais

#trocando iformações entre var
var1 = 54
var2 = 76

var1, var2 = var2, var1

print(var1)
print(var2)


#operador condicional ternário 
menor = var1 if var1 < var2 else var2
print(menor)
print({(var1,var1)[var1<var2]})  

#generators
valores = [1,23,54,6,5,23,54]
quadrado = (item**2 for item in valores)
for valor in quadrado:
    print(valor)  


#função enumerate - retorna indice e nomes 

cores = ['vermelho','amerelo','preto','rosa']
for i, t in enumerate(cores):
    print(i,t)

temp = [-2,21,-5,7,4,-8]
for x,z in enumerate(temp):
    if z<0:
        print(f'cidade {x} está abaixo de zero com {z}')


#gerenciamento de contexto com with

with open('usando_var.txt','r', encoding= 'utf-8') as a:
    for linha in a:
        print(linha, end='')
