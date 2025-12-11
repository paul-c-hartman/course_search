import json
import embeddings
import db

# Connect to MongoDB
database = db.get_db()
course_data = database['courses']

# Import course data from data/courses.json
print("Loading course data... ")
with open('data/courses.json', 'r') as f:
    courses = json.load(f)
courses = courses[1:] # Skip the first entry, it's not a course
print("Done. Found {} courses.".format(len(courses)))
# Store course data in MongoDB
print("Storing course data in MongoDB... ")
course_data.insert_many(courses)
print("Done.")

# Generate embeddings for each course description
print("Generating embeddings for course descriptions... ")
embeddings_list = []
for course in courses:
    description = course.get('description', '')
    embedding = embeddings.get_embedding(description)
    embeddings_list.append({
        'course_code': course.get('code'),
        'embedding': embedding
    })
print("Done. Generated embeddings for {} courses.".format(len(embeddings_list)))
# Store embeddings in MongoDB
print("Storing embeddings in MongoDB... ")
embedding_data = database['embeddings']
embedding_data.insert_many(embeddings_list)
print("Done.")