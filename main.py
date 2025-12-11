import lib.db as db
import lib.embeddings as embeddings
import math

def cosine_similarity(vec1, vec2):
    dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))
    magnitude_vec1 = math.sqrt(sum(v1**2 for v1 in vec1))
    magnitude_vec2 = math.sqrt(sum(v2**2 for v2 in vec2))

    if magnitude_vec1 == 0 or magnitude_vec2 == 0:
        return 0
    else:
        return dot_product / (magnitude_vec1 * magnitude_vec2)

def main():
    # Load embeddings from MongoDB
    print("Load embeddings from MongoDB...")
    database = db.get_db()
    embedding_collection = database['embeddings']
    all_embeddings = list(embedding_collection.find({}))
    course_collection = database['courses']
    print(f"Loaded {len(all_embeddings)} embeddings.")
    
    # Simple REPL to similarity-search the embeddings
    while True:
        query = input("Enter your query (or 'q' to quit): ")
        if query.lower() == 'q':
            break

        query_embedding = embeddings.get_embedding(query)
        similarities = []
        for item in all_embeddings:
            item_embedding = item['embedding']
            similarity = cosine_similarity(query_embedding, item_embedding)
            similarities.append((similarity, item))
        
        similarities.sort(key=lambda x: x[0], reverse=True)
        print(f"Found {len(similarities)} results:")
        for similarity, embedding in similarities[:3]:  # Show top 3 results
            course = course_collection.find_one({'code': embedding['course_code']})
            print(f"Similarity: {similarity:.4f}, Course: {embedding['course_code']} - {course['title']}")

if __name__ == "__main__":
    main()
