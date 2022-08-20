import mysql.connector as conn

db = conn.connect(host='localhost', user='root', password='MuRali0423', database='task')
cursor = db.cursor()
#q1 = "select * from users"
q = 'delete from users where `index`=%s'
val = ("7",)
cursor.execute(q,val)
# db.commit()
# cursor.execute(q1)
# for i in cursor.fetchall():
#     print(i)
db.close()