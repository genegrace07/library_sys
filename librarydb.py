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
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def sign_in(self,username,password):
        db.ping(reconnect=True)
        cursor = db.cursor(dictionary=True,buffered=True)
        value = 'insert into admins(username,password) values(%s,%s)'
        cursor.execute(value,(username,password))
        db.commit()
        cursor.close()

    def login_in(self,username):
        db.ping(reconnect=True)
        cursor = db.cursor(dictionary=True,buffered=True)
        pass
