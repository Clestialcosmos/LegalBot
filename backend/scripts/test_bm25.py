from app.rag.storage import load_chunks, load_bm25

chunks = load_chunks()
bm25 = load_bm25()

query = "What is FIR"

docs = bm25.search(query, k=10)

for i, doc in enumerate(docs, 1):
    print("=" * 80)
    print(i)
    print(doc.metadata)
    print(doc.page_content[:700])