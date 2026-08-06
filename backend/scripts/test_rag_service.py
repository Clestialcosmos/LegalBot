from app.services.rag_service import RAGService

rag = RAGService()

question = "What is anticipatory bail?"

response = rag.ask(question)

print("\nQUESTION:")
print(question)

print("\nANSWER:")
print(response["answer"])

print("\nSOURCES:")

for doc in response["documents"]:
    print(
        f"{doc.metadata['source']} "
        f"(Page {doc.metadata['page']})"
    )