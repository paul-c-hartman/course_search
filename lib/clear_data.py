from pymongo import MongoClient

print("Clearing database...")
try:
    client = MongoClient('mongodb', 27017, username='root', password='rootpassword')
    client.drop_database('courses_db')
    print("Successfully cleared database")
except:
    print("Failed to clear database")