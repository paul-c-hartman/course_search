import ollama

def get_embedding(text):
    client = ollama.Client('http://localhost:11434')
    response = client.embeddings(
        model='mxbai-embed-large',
        prompt=text
    )
    return response['embedding']