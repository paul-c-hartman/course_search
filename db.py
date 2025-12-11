from pymongo import MongoClient

def get_db():
    client = MongoClient('localhost', 27017, username='root', password='rootpassword')

    db = client['courses_db']
    return db