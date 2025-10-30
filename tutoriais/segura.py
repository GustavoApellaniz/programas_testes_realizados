funcionarios = {
    "Alice": {"salario": 5000, "ferias_restantes": 15, "departamento": "TI"},
    "Bruno": {"salario": 4500, "ferias_restantes": 10, "departamento": "Financeiro"},
    "Carlos": {"salario": 6000, "ferias_restantes": 20, "departamento": "Marketing"},
    "Diana": {"salario": 7000, "ferias_restantes": 5, "departamento": "Vendas"},
    "Eduardo": {"salario": 5500, "ferias_restantes": 12, "departamento": "TI"}
}
funcionarios['fernanda'] = {
    "salario": 6000,
    "ferias_restantes": 30,
    "departamento": "Recursos Humanos"
}

print(funcionarios["fernanda"])

if funcionarios["Carlos"]:
    print('ele está na lista')
else:
    print('não existe')

print('Carlos' in funcionarios)