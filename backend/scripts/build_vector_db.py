from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.vector_store import create_vector_store

print("Loading PDFs...")
documents = load_documents()

print("\nSplitting documents...")
chunks = split_documents(documents)

print("\nBuilding FAISS index...")
create_vector_store(chunks)

print("\nDone!")