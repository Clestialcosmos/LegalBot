from app.rag.loader import load_documents

docs = load_documents()

keywords = [
    "first information report",
    "information relating to commission of cognizable offence",
]

for doc in docs:
    text = doc.page_content.lower()

    for key in keywords:
        if key in text:
            print("=" * 80)
            print("Keyword:", key)
            print(doc.metadata)
            print(doc.page_content[:1500])
            break