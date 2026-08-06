from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.bm25 import BM25Retriever
from app.rag.retriever import load_vector_store
from app.rag.fusion.rrf import reciprocal_rank_fusion

# -----------------------------
# Load and prepare documents
# -----------------------------
print("Loading documents...")
documents = load_documents()

print("\nSplitting documents...")
chunks = split_documents(documents)

print("\nBuilding BM25 index...")
bm25 = BM25Retriever(chunks)

print("\nLoading FAISS index...")
vector_store = load_vector_store()

# -----------------------------
# Query
# -----------------------------
query = "What is anticipatory bail?"

print(f"\nQuery: {query}")

# -----------------------------
# Retrieve from FAISS
# -----------------------------
faiss_results = vector_store.similarity_search(query, k=5)

# -----------------------------
# Retrieve from BM25
# -----------------------------
bm25_results = bm25.search(query, k=5)

# -----------------------------
# Hybrid Fusion
# -----------------------------
hybrid_results = reciprocal_rank_fusion(
    faiss_results,
    bm25_results
)

# -----------------------------
# Print Results
# -----------------------------
for i, doc in enumerate(hybrid_results[:5], start=1):
    print("\n" + "=" * 80)
    print(f"Hybrid Result {i}")
    print("=" * 80)

    print(f"Source : {doc.metadata.get('source')}")
    print(f"Page   : {doc.metadata.get('page')}")

    print("\nContent:\n")
    print(doc.page_content[:800])