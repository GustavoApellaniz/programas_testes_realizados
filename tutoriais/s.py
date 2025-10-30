


try:
    man = open('C:\\Users\\Teste_01\\OneDrive\\Desktop\\arq.txt.txt', 'a', encoding= 'utf-8')
    man.write('\ntristeza')
except IOError:
    print('erro')
else:
    man.close()

try:
    man = open('C:\\Users\\Teste_01\\OneDrive\\Desktop\\arq.txt.txt', 'r', encoding= 'utf-8')
    print(man.read())
except IOError:
    print('erro')
else:
    man.close()

