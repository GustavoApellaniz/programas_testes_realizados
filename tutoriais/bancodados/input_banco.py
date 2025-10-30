import mysql.connector
from mysql.connector import Error

con = mysql.connector.connect(host = 'localhost', database ='world', user = 'root',                         password = 'Ap@17122022')

try: 
    a = input('coloque o Name ')
    b = input('coloque o country ')
    c = input('coloque o district ')

    dados =  '\'' + a + '\'' + ", '" + b + "' ," +  '\'' + c + '\'' + ')'


    declaraçao = '''insert into city (Name, CountryCode, District)
    values(
    '''
    sql = declaraçao + dados
    z = con.cursor()
    z.execute(sql)
    con.commit()
    
    print(z.rowcount,' numero de dados adicionnados!!!!@E$@##@$')
    z.close()
except Error as e:
    print('sujo',format(e))
finally:
    con.close()
    print('integração encerrada @#&¨&¨$!#@%¨!@(#!*@#!@)')