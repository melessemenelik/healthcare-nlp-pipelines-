from fastapi import FastAPI
from preprocessing import preprocess_text
from embeddings import get_embeddings
from retrieval import search

app = FastAPI()

@app.post("/query")
def query_pipeline(text: str):
    tokens = preprocess_text(text)
    embedding = get_embeddings(tokens)
    results = search(embedding)
    return {"results": results}
