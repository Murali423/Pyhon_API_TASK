import pymongo
from flask import Flask,request,jsonify
import logging

logging.basicConfig(filename='mangotask.log',level=logging.DEBUG,
                    format='[%(asctime)s]:%(name)s: %(levelname)s:%(message)s')

app = Flask(__name__)

@app.route('/mongo/insert',methods=['GET','POST'])
def mongo_insert():
    if request.method == 'POST':
        logging.debug('This Method will insert records to Mongodb')
        try:
            logging.debug('Createing connection for mongodb an testing the connection')
            client = pymongo.MongoClient(
                "mongodb+srv://murali:mongodb123@cluster0.fxgp1cv.mongodb.net/?retryWrites=true&w=majority")
            logging.info('Connection is')
            db = client.test
            logging.info(db)
            logging.debug('creating the new database and collection for database')
            db_mng = client['mongotest']
            coll = db_mng['test3']
            a = request.json['id']
            b = request.json['name']
            c = request.json['salary']
            print(a,b,c)
            logging.info(request.json)
            coll.insert_one(request.json)
            logging.info('Inserstion to mongodb is successful')
            logging.info('retriving values for logs')
            record = coll.find()
            l = []
            for i in record:
                logging.info(i)
                l.append(i)
        except Exception as e:
            logging.exception(e)
        return jsonify("Record inserted to mongodb is successful", str(l))

@app.route('/mongo/update',methods=['GET','POST'])
def mongo_update():
    if request.method == 'POST':
        logging.debug('This Method will update records to Mongodb')
        try:
            logging.debug('Createing connection for mongodb an testing the connection')
            client = pymongo.MongoClient(
                "mongodb+srv://murali:mongodb123@cluster0.fxgp1cv.mongodb.net/?retryWrites=true&w=majority")
            logging.info('Connection is')
            db = client.test
            logging.info(db)
            logging.debug('creating the new database and collection for database')
            db_mng = client['mongotest']
            coll = db_mng['test3']
            a = request.json['id']
            b = request.json['name']
            c = request.json['salary']
            print(a, b, c)
            logging.info(request.json)
            filter = {'id': a}
            newvalues = {"$set":{"salary":c}}
            coll.update_one(filter,newvalues)
            logging.info(f' Salary of Record has updated to {c} having id {a} is successful')
            logging.info('retriving values for logs')
            record = coll.find()
            l = []
            for i in record:
                logging.info(i)
                l.append(i)
        except Exception as e:
            logging.exception(e)
        return jsonify("Record Updated to mongodb is successful", str(l))

#data {id:6}
@app.route('/mongo/delete', methods=['GET','POST'])
def mongo_delete():
    if request.method == 'POST':
        logging.debug('This Method will delete records based on id in Mongodb')
        try:
            logging.debug('Creating connection for mongodb an testing the connection')
            client = pymongo.MongoClient(
                "mongodb+srv://murali:mongodb123@cluster0.fxgp1cv.mongodb.net/?retryWrites=true&w=majority")
            logging.info('Connection is')
            db = client.test
            logging.info(db)
            logging.debug('creating the new database and collection for database')
            db_mng = client['mongotest']
            coll = db_mng['test3']
            a = request.json['id']
            print(a,)
            logging.info(request.json)
            coll.delete_one(request.json)
            logging.info(f' Record having id {a} is successfully Deleted')
            logging.info('retrieving values for logs')
            record = coll.find()
            l = []
            for i in record:
                logging.info(i)
                l.append(i)
        except Exception as e:
            logging.exception(e)
        return jsonify("Records after successful deletion of data", str(l))


# data {id:7}
@app.route('/mongo/fetch', methods=['GET', 'POST'])
def mongo_fetch():
    if request.method == 'POST':
        logging.debug('This Method will fetch record based on id from Mongodb')
        try:
            logging.debug('Creating connection for mongodb an testing the connection')
            client = pymongo.MongoClient(
                "mongodb+srv://murali:mongodb123@cluster0.fxgp1cv.mongodb.net/?retryWrites=true&w=majority")
            logging.info('Connection is')
            db = client.test
            logging.info(db)
            logging.debug('creating the new database and collection for database')
            db_mng = client['mongotest']
            coll = db_mng['test3']
            a = request.json['id']
            print(a)
            logging.info(request.json)
            m = coll.find_one(request.json)
            logging.info(f' Record having id/salary {a} is successfully fetched')
            logging.info('retrieving values for logs'+str(m))
        except Exception as e:
            logging.exception(e)
        return jsonify("Record fetched from Mongodb is ", str(m))

    if request.method == 'GET':
        logging.debug('This Method will fetch record based on id from Mongodb')
        try:
            logging.debug('Creating connection for mongodb an testing the connection')
            client = pymongo.MongoClient(
                "mongodb+srv://murali:mongodb123@cluster0.fxgp1cv.mongodb.net/?retryWrites=true&w=majority")
            logging.info('Connection is')
            db = client.test
            logging.info(db)
            logging.debug('creating the new database and collection for database')
            db_mng = client['mongotest']
            coll = db_mng['test3']
            record = coll.find()
            l = []
            for i in record:
                logging.info(i)
                l.append(i)
        except Exception as e:
            logging.exception(e)
        return jsonify("Records fetched from Mongodb are ", str(l))


if __name__ == '__main__':
    app.run()