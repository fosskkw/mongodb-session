import pymongo
import time


try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    myclient.admin.command("ping")

    # print("Connected successfully")
except Exception as error:
    print('Connection to the databases failed')
    print('Error: ', error)
    time.sleep(5)


def get_db():
    mydb = myclient['application']
    mycol = mydb['users']

    return mycol