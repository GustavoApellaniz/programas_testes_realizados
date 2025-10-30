import mysql.connector

con = mysql.connector.connect(host = 'localhost', database ='world', user = 'root',                         password = 'Ap@17122022')

    #conectando o my_sql no python 
'''
if con.is_connected():
    a =con.server_info
    print('informações do server', a)
    b = con.cursor()
    b.execute('select database();')
    c = b.fetchone()
    print('estamos no banco', c)


if con.is_connected():
    b.close()
    con.close()
    print('kill myself')

'''

    #criando uma tabela no python - não usual esta porra 
try:
    #usado para criar a estrutura no banco de dados nesta...
    a = '''create table usando_py(   
    exemplo int not null,
    primary key(exemplo),
    vida varchar(20),
    morte int,
    data date )
    '''
    b =con.cursor()
    b.execute(a)
except mysql.connector.Error as erro:
    print(format(erro))
finally:
    if con.is_connected():
        con.close()
        b.close()
        print('ação encerrada')


        

