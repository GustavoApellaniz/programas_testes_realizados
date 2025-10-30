#seguinte: tenha em mente que o flask sera usado apenas para complementar o mysql.connector por agora

import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

con = mysql.connector.connect(host = 'localhost', database ='escola_online', user = 'root',                         password = 'Ap@17122022')
@app.route('/get_table', methods =['GET'])

def get_table():
    cur = con.cursor()
    cur.execute('show tables;')
    table = cur.fetchall()
    cur.close()
    nomes = [t[0] for t in table]
    return jsonify(nomes)
        
    


if __name__ == '__main__':
   app.run(debug=True)
    