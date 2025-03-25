import ollama
import db
from models import *

def ask_ollama(question, llm = "llama2"):
    response = ollama.chat(model=llm, messages=[{
        'role': 'user',
        'content': question,
    },])
    return response['message']['content']

def embed_ollama(text):
    response = ollama.embed(model='mxbai-embed-large', input=text)
    embeddings = response["embeddings"]

    emb = Embedding(
        embeddings=embeddings,
        documents=[text]
    )

    emb.save()

def mass_embed(texts):
    documents = db.get_notes

    for _, d in enumerate(documents):
        response = ollama.embed(model="mxbai-embed-large", input=d)
        embeddings = response["embeddings"]
        
        emb = Embedding(
            embeddings=embeddings,
            documents=[d]
        )

        emb.save()