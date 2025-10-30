import mysql.connector

con = mysql.connector.connect(host = 'localhost', database ='world', user = 'root', password = 'Ap@17122022')

ins = '''insert into city ( Name, CountryCode , District, Population)
values
('Valmont', 'USA', 'Colorado', 48500),
('Serra Azul', 'BRA', 'São Paulo', 31200),
('Miyagawa', 'JPN', 'Gifu', 17600),
('Port Hope', 'CAN', 'Ontario', 23600),
('Borgovia', 'ITA', 'Lombardia', 52900);
'''
cur = con.cursor()
cur.execute(ins)
con.commit()
print(cur.rowcount,'registros inseridos na tabela')
cur.close()
con.close()


