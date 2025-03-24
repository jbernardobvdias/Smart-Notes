import ollama

def ask_ollama(question, llm = "llama2"):
    response = ollama.chat(model=llm, messages=[{
        'role': 'user',
        'content': question,
    },])
    print(response['message']['content'])

def embed_ollama():
    ollama.embed(
        model='mxbai-embed-large', 
        input='Llamas are members of the camelid family',
    )