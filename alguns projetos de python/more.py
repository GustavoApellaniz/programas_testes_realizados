#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um
#programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import randint

alunos = ['rogerio','lucas','leo','luciano','Gustavo']
aleatorio = randint(0, len(alunos)-1)
escolha = alunos[aleatorio]
print(f'{escolha}')

x = randint(0,9999)
y=x
for i in str(y):
    print(i)