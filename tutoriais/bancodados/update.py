import mysql.connector
from mysql.connector import Error

def conect():
    try:
        global con
        con = mysql.connector.connect(host = 'localhost', database ='cadastro', user = 'root', password = 'Ap@17122022')
    except Error as e:
        print('erro no login', format(e))

def consulta(x):
    try:
        conect()
        z = 'select * from cursos where idcurso =' +  x
        cur = con.cursor()
        cur.execute(z)
        linhas = cur.fetchall()
        for linha in linhas:
            print(linha,'\n') 
    except Error as e:
        print('erro na busca', format(e))
    finally:
        if con.is_connected:
            con.close()
            cur.close()

def atualizacao(b):
    try:
        conect()
        alterar = b
        cur = con.cursor()
        cur.execute(alterar)
        con.commit()
        print('dados alterados')
    except Error as e:
        print('Houve algum erro na mudança',format(e))
    finally:
        if con.is_connected():
            con.close()
            cur.close()
           


if __name__ == '__main__':

    z = input('id das aulas ')
    consulta(z)

    print('digite sua nova carga horária ')
    x = input()  

    declaracao = '''update cursos set carga = ''' + x + ''' where idcurso = ''' + z
    atualizacao(declaracao)
    consulta(z)

