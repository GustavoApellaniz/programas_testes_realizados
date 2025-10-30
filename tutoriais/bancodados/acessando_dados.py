import mysql.connector


con = mysql.connector.connect(host = 'localhost', database ='world', user = 'root', password = 'Ap@17122022')
 
try:
    c = 'select * from city'
    cur = con.cursor()
    cur.execute(c)
    l = cur.fetchall()
    print('numero total de registros', cur.rowcount)

    for linhas in l:
        print('name:', linhas[0])
        print('countrycode:',linhas[1])
        print('population:',linhas[2], '\n')
except mysql.connector.Error as e:
    print('erro')
finally:
    if con.is_connected():
        con.close()
        cur.close()
        print('encerrado')

    




