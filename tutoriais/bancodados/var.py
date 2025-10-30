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
        return cur.fetchall() 
    except Error as e:
        print('erro na busca', format(e))
    finally:
        if con.is_connected:
            con.close()
            cur.close()


if __name__ == '__main__':
    z = input()
    print(consulta(z))
    



