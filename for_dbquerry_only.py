import mysql.connector
from dotenv import load_dotenv
import os
import json

load_dotenv()

db = mysql.connector.connect(
    host = os.getenv('dbhost'),
    user = os.getenv('dbuser'),
    password = os.getenv('dbpassword'),
    database = os.getenv('dbname')
)

dbcursor = db.cursor()
dbcursor.execute('select * from books')
result_querry = dbcursor.fetchall()
print(result_querry)

#import json data to mysql
books_json = 'books.json'
with open(books_json,"r") as f:
    data = json.load(f)

for l in data:
    #print(l)
    dbcursor.execute("""insert into books(book_id,title,author,status) values(%s,%s,%s,%s)
                     ON DUPLICATE KEY UPDATE
                     title=values(title),
                     author=values(author),
                     status=values(status)
                     """,(l['book_id'],l['title'],l['author'],l['status']))

# db.commit()
# dbcursor.close()
# db.close()




