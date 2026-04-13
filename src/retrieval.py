import faiss
import numpy as np

# Build FAISS index
dimension = 768
index = faiss.IndexFlatL2(dimension)

def add_embeddings(embeddings):
    index.add(np.array(embeddings))

def search(query_embedding, k=5):
    distances, indices = index.search(np.array([query_embedding]), k)
    return distances, indices
