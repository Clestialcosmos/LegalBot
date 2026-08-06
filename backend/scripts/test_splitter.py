from app.rag.loader import load_documents
from app.rag.splitter import split_documents

documents = load_documents()

chunks = split_documents(documents)

print(f"\nTotal Chunks: {len(chunks)}")

print("\n" + "=" * 80)
print("FIRST CHUNK")
print("=" * 80)

print(chunks[0].page_content)

print("\nMetadata")
print(chunks[0].metadata)

print("\nChunk Length")
print(len(chunks[0].page_content))