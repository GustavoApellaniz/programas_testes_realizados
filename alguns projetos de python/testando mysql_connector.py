import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

con = mysql.connector.connect(host = 'localhost', database ='escola_online', user = 'root',                         password = 'Ap@17122022')
@app.route('/')

def index():
   return 'hellow world'
    


if __name__ == '__main__':
   app.run()
    