import os 

os.chdir('C:\\trabdentro')
print(f'seu dir é {os.getcwd()}')

nome = input("escolha o nome que deseja para seu arquivos ")

for contdor, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, exten_arq = os.path.splitext(arq)
        nome_arq = nome +' '+ str(contdor)

        nome_novo = f'{nome_arq}{exten_arq}'
        os.rename(arq, nome_novo)

print(f'arquivos renomeados')