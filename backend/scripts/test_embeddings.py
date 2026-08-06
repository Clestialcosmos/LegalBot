from app.rag.embeddings import get_embedding_model

embeddings = get_embedding_model()

query = "What is anticipatory bail?"

vector = embeddings.embed_query(query)

print(f"Query: {query}")
print(f"Embedding Dimension: {len(vector)}")
print("\nFirst 10 values:")
print(vector[:10])