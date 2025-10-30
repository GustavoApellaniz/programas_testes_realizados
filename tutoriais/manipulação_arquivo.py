# manipulação de arquivo de texto
 
# função open() - retorna o objeto chamado de manipulador de arquivos
'''
modos de acesso:
| Modo | Significado                                                                                                                     |
| ---- | ------------------------------------------------------------------------------------------------------------------------------- |
| `r`  | Somente leitura                                                                                                                 |
| `r+` | Leitura e escrita. O texto é inserido no início do arquivo.                                                                     |
| `w`  | Escrita, apagando (truncando) o conteúdo existente no arquivo.                                                                  |
| `w+` | Leitura e escrita. O arquivo é criado, se não existir; se existir, é truncado. O texto é inserido no início do arquivo.         |
| `a`  | Escrita, preservando o conteúdo existente (append). O arquivo é criado, se não existir. O texto é inserido no final do arquivo. |
| `b`  | Modo binário.                                                                                                                   |
| `+`  | Atualização – leitura e escrita.                                                                                                |
| `x`  | Abre o arquivo para criação exclusiva, falhando se o arquivo já existir.                                                        |
'''

#escrever em arquivos de texto

texto = ('bad day son?')
try:
    man = open('usando_var.txt','w', encoding= 'utf-8')
    man.write(texto)
except IOError:
    print('arquivo não encontrado')
else:
    man.close()

try:
    man = open('usando_var.txt','r', encoding= 'utf-8')
    print(man.read())
except IOError:
    print('arquivo não encontrado')
else:
    man.close()




 