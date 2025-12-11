import ollama
import os

# Setup
model = os.getenv('EMBEDDING_MODEL', 'nomic-embed-text')
client = ollama.Client('http://ollama:11434')
print(f"Asking for model: {model}. This might take a bit")
try:
    client.pull(model)
    print("Model loaded successfully")
except Exception as e:
    print(f"Failed to pull model: {e}")
    raise e

def get_embedding(text):
    client = ollama.Client('http://ollama:11434')
    response = client.embeddings(
        model=model,
        prompt=text
    )
    return response['embedding']