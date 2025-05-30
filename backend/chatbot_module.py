from utils.embedder import get_embedding
from utils.ollama_chain import ask_ollama
from utils.openai_chain import ask_openai

def handle_query(user_input, engine="ollama"):
    embedding = get_embedding(user_input)
    context = "mocked context from vector search"
    return ask_openai(user_input, context) if engine == "openai" else ask_ollama(user_input, context)
