import pickle

from app.rag.loader import load_documents
from app.rag.splitter import split_documents


print("Loading PDFs...")
documents = load_documents()

print("Splitting documents...")
chunks = split_documents(documents)

with open("data/processed/chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print(f"Saved {len(chunks)} chunks to data/processed/chunks.pkl")