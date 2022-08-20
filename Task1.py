import logging
from flask import Flask,request,jsonify
import mysql.connector as conn


logging.basicConfig(filename='Task.log',level=logging.DEBUG,
                    format='[%(asctime)s]: %(levelname)s:%(name)s:%(message)s')

"""1 . Write a program to insert a record in sql table via api database
2.  Write a program to update a record via api 
3 . Write a program to delete a record via api 
4 . Write a program to fetch a record via api
5 . All the above questions you have to answer for mongo db as well ."""
app = Flask(__name__)
@app.route('/abc/insert',methods=['GET','POST'])
def insert():
    if (request.method == 'POST'):
        logging.info('This method to insert the data into the mysql')
        try:
            logging.info('Creating the connection to mysql database')
            db = conn.connect(host='localhost', user='root', password='MuRali0423', database='task')
            logging.info(db)
            logging.info('Connection to mysql is successful')
            a = request.json['index']
            b = request.json['Region']
            c = request.json['Manager']
            cursor = db.cursor()
            q = "insert into users (`index`,`Region`,`Manager`) values (%s, %s, %s)"
            val = (a,b,c)
            cursor.execute(q,val)
            db.commit()
            q1 = 'select * from users'
            cursor.execute(q1)
            for i in cursor.fetchall():
                logging.info(i)

        except Exception as e:
            logging.exception(e)
            db.rollback()
        finally:
            db.close()
            print('Inserted successfully')
        return jsonify("Insert is successful")
#data: {
#     "index": 5,
#     "Region":"Karnatak",
#     "Manager":"Ineuron"
# }

@app.route('/abc/update',methods=['GET','POST'])
def update_rec():
    if request.method == 'POST':
        logging.debug('This method will Update the data into the mysql')
        try:
            logging.info('Creating the connection to mysql database')
            db = conn.connect(host='localhost', user='root', password='MuRali0423', database='task')
            logging.info(db)
            logging.info('Connection to mysql is successful')
            cursor = db.cursor()
            q1 = 'select * from users'
            logging.info('Before updating the value')
            cursor.execute(q1)
            for i in cursor.fetchall():
                logging.info(i)
            a = request.json['index']
            b = request.json['Region']
            c = request.json['Manager']
            q = "update users SET `Region`= %s where `index`= %s or `Manager`= %s "
            val = (b, a, c)
            cursor.execute(q, val)
            db.commit()
            q1 = 'select * from users'
            cursor.execute(q1)
            logging.info('After updating the value')
            for i in cursor.fetchall():
                logging.info(i)

        except Exception as e:
            logging.exception(e)
            db.rollback()
        finally:
            db.close()
            print('Updated successfully')
        return jsonify("Update is successful")

#data: {
#     "index": 7,
#     "Region":"DL1",
#     "Manager":"Ineuron"
# }

@app.route('/abc/delete',methods=['GET','POST'])
def delete_rec():
    if request.method == 'POST':
        try:
            logging.info('Creating the connection to mysql database')
            db = conn.connect(host='localhost', user='root', password='MuRali0423', database='task')
            logging.info(db)
            logging.info('Connection to mysql is successful')
            cursor = db.cursor()
            q1 = 'select * from users'
            logging.info('Before deleting the value')
            cursor.execute(q1)
            for i in cursor.fetchall():
                logging.info(i)
            a = request.json['index']
            q = "delete from users where `index`= %s "
            val = (a,)
            cursor.execute(q, val)
            db.commit()
            q1 = 'select * from users'
            cursor.execute(q1)
            logging.info('After deleting the value')
            for i in cursor.fetchall():
                logging.info(i)

        except Exception as e:
            logging.exception(e)
            db.rollback()
        finally:
            db.close()
            print('Record Deleted successfully')
        return jsonify("Record Deleted successful")


@app.route('/abc/fetch',methods=['GET','POST'])
def fetch_rec():
    if request.method == 'POST':
        logging.debug('This Method is used to fetch records based on id')
        try:
            logging.info('Creating the connection to mysql database')
            db = conn.connect(host='localhost', user='root', password='MuRali0423', database='task')
            logging.info(db)
            logging.info('Connection to mysql is successful')
            a = request.json['index']
            print(request.json)
            cursor = db.cursor()
            q1 = 'select * from users where `index`=%s'
            val = (a,)
            cursor.execute(q1, val)
            m = cursor.fetchone()
            print(m)
            logging.info(m)
        except Exception as e:
            logging.exception(e)
            db.rollback()
        finally:
            db.close()
            print('Record Displayed successfully')
        return jsonify("Record Displayed successful", str(m))

    if request.method == 'GET':
        logging.debug('This Method is used to fetch all records')
        try:
            logging.info('Creating the connection to mysql database')
            db = conn.connect(host='localhost', user='root', password='MuRali0423', database='task')
            logging.info(db)
            logging.info('Connection to mysql is successful')
            cursor = db.cursor()
            q1 = 'select * from users'
            cursor.execute(q1)
            m = cursor.fetchall()
            l = []
            for i in m:
                l.append(i)
            print('All records',l)
            logging.info(l)
        except Exception as e:
            logging.exception(e)
            db.rollback()
        finally:
            db.close()
            print('Records Displayed successfully')
        return jsonify("Records Displayed successful", str(l))


if __name__ == '__main__' :
    app.run()



