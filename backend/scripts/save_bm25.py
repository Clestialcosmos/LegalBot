import pickle

from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.bm25 import BM25Retriever

print("Loading PDFs...")
documents = load_documents()

print("Splitting documents...")
chunks = split_documents(documents)

print("Building BM25...")
bm25 = BM25Retriever(chunks)

with open("data/processed/bm25.pkl", "wb") as f:
    pickle.dump(bm25, f)

print("BM25 saved successfully!")