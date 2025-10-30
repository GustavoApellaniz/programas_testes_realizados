#Escreva um programa que calcule o faturamento de um representante comercial que recebe R$ 500,00 
#fixos e 6% de comissão sobre as vendas do mês. Considere que ele fechou o mês 
#com um valor de R$ 12.398,00 em vendas. Ao final, exiba o resultado.

y = float(input("quantas vendas no mês?"))
x = 500 + (y * 0.06)
print(f'o valor total no final foi {x:.2f}')

