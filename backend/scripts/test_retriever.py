from app.rag.retriever import retrieve_documents

query = "Can property be transferred orally?"

results = retrieve_documents(query)

print(f"\nQuery: {query}")

for doc in results:
    print(doc.metadata)
    print("-" * 50)