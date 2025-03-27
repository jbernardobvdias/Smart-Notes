import ollama
import numpy as np
from backend.data.db import *
from backend.models import *

def ask_ollama(question, llm = "llama2"):
    response = ollama.chat(model=llm, messages=[{
        'role': 'user',
        'content': question,
    },])
    return response['message']['content']

def generate_embedding(text):
    response = ollama.embeddings(model='mistral', prompt=text)
    embedding = np.array(response['embedding'], dtype=np.float32)
    return embedding.tobytes()

def add_embedding(sender, instance, **kwargs):
    # Only generate if not already present
    if not instance.embedding:  
        instance.embedding = generate_embedding(instance.text)

def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_a = np.linalg.norm(vec1)
    norm_b = np.linalg.norm(vec2)
    return dot_product / (norm_a * norm_b)

def find_similar_notes(query_text, threshold=0.8):
    query_embedding = generate_embedding(query_text)
    query_vector = np.frombuffer(query_embedding, dtype=np.float32)

    notes = Note.objects.exclude(embedding__isnull=True)

    similar_notes = []
    for note in notes:
        note_vector = np.frombuffer(note.embedding, dtype=np.float32)
        similarity = cosine_similarity(query_vector, note_vector)
        if similarity >= threshold:
            similar_notes.append((note, similarity))

    similar_notes.sort(key=lambda x: x[1], reverse=True)
    return [note[0] for note in similar_notes]