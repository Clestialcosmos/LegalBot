from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.bm25 import BM25Retriever
from app.rag.retriever import load_vector_store
from app.rag.fusion.rrf import reciprocal_rank_fusion
from app.rag.prompt_builder import build_prompt

query = "What is anticipatory bail?"

documents = load_documents()
chunks = split_documents(documents)

bm25 = BM25Retriever(chunks)
vector_store = load_vector_store()

faiss_docs = vector_store.similarity_search(query, k=5)
bm25_docs = bm25.search(query, k=5)

docs = reciprocal_rank_fusion(faiss_docs, bm25_docs)

prompt = build_prompt(query, docs)

print(prompt)