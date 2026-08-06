from app.rag.loader import load_documents

docs = load_documents()

print(f"\nTotal pages: {len(docs)}")

for page in [0, 1, 2, 10]:
    print("\n" + "=" * 60)
    print(f"Page: {page}")
    print(f"Source: {docs[page].metadata['source']}")
    print("-" * 60)
    print(docs[page].page_content[:700])