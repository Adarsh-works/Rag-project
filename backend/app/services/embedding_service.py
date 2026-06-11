import requests

OLLAMA_URL = "http://localhost:11434/api/embed"
MODEL_NAME = "nomic-embed-text"


def get_embedding(text: str):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "input": text
        }
    )

    response.raise_for_status()

    return response.json()["embeddings"][0]