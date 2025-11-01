import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db = mysql.connector.connect(
    host = os.getenv('dbhost'),
    user = os.getenv('dbuser'),
    password = os.getenv('dbpassword'),
    database = os.getenv('dbname')
)
# dbcursor = db.cursor()
# dbcursor.execute('select * from books')
# result = dbcursor.fetchall()

class Users:
    def sign_up(self,username,password):
        db.ping(reconnect=True)
        cursor = db.cursor(dictionary=True,buffered=True)
        value = 'insert into admins(username,passwd) values(%s,%s)'
        cursor.execute(value,(username,password))
        db.commit()
        cursor.close()
    # def login_in(self,username,hashpassword):
    #     db.ping(reconnect=True)
    #     cursor = db.cursor(dictionary=True,buffered=True)
    #     querry = 'select username,passwd from books where username = %s and passwd = %s'
    #     cursor.execute(querry,(username,hashpassword,))
    #     result = cursor.fetchone()
    #     cursor.close()
    #     return  result
    def get_username(self,username):
        db.ping(reconnect=True)
        cursor = db.cursor(dictionary=True,buffered=True)
        querry = 'select * from admins where username = %s'
        cursor.execute(querry,(username,))
        result = cursor.fetchone()
        cursor.close()
        return result