import logging

from app.rag.retriever import load_vector_store
from app.rag.fusion.rrf import reciprocal_rank_fusion
from app.rag.prompt_builder import build_prompt
from app.ai.groq_client import generate_response
from app.rag.storage import load_chunks, load_bm25

from app.services.language_service import detect_language

from app.ai.translator import (
    translate_to_english,
    translate_from_english,
)

from app.middleware.safety import (
    check_emergency,
    is_legal_query,
)

from app.memory.memory import ConversationMemory

logger = logging.getLogger(__name__)


class RAGService:

    def __init__(self):

        logger.info("Initializing LegalBot RAG...")

        self.chunks = None

        self.bm25 = None

        self.vector_store = None

        self.memory = ConversationMemory()

        logger.info("LegalBot initialized successfully.")
    def initialize(self):

        if self.vector_store is None:

            logger.info("Loading RAG resources...")

            self.chunks = load_chunks()

            self.bm25 = load_bm25()

            self.vector_store = load_vector_store()

            logger.info("RAG resources loaded.")
    def retrieve(
        self,
        query: str,
        k: int = 5,
    ):

        faiss_docs = self.vector_store.max_marginal_relevance_search(
            query=query,
            k=k,
            fetch_k=20,
        )

        bm25_docs = self.bm25.search(
            query=query,
            k=k,
        )

        fused_docs = reciprocal_rank_fusion(
            faiss_docs,
            bm25_docs,
        )

        unique_docs = []

        seen = set()

        for doc in fused_docs:

            key = (
                doc.metadata.get("source"),
                doc.metadata.get("page"),
            )

            if key not in seen:

                seen.add(key)

                unique_docs.append(doc)

        return unique_docs[:k]

    def ask(
        self,
        query: str,
    ):

        original_query = query.strip()
        self.initialize()
        if not original_query:

            return {
                "answer": "Please enter a legal question.",
                "documents": [],
                "sources": [],
                "language": "en",
                "original_query": "",
            }

        language = detect_language(
            original_query
        )

        emergency = check_emergency(
            original_query
        )

        if emergency:

            answer = emergency["answer"]

            if language in ["hi", "hinglish"]:

                answer = translate_from_english(
                    answer,
                    language,
                )

            return {
                "answer": answer,
                "documents": [],
                "sources": [],
                "language": language,
                "original_query": original_query,
            }

        history = self.memory.history()

        if not is_legal_query(original_query):

            if not history:

                answer = (
                    "I am LegalBot. I can answer only "
                    "Indian legal questions."
                )

                if language in ["hi", "hinglish"]:

                    answer = translate_from_english(
                        answer,
                        language,
                    )

                return {
                    "answer": answer,
                    "documents": [],
                    "sources": [],
                    "language": language,
                    "original_query": original_query,
                }

        retrieval_query = original_query

        if language in ["hi", "hinglish"]:

            retrieval_query = translate_to_english(
                original_query
            )

        search_query = retrieval_query

        if history:

            last_user = self.memory.last_user_message()

            if (
                last_user
                and last_user.lower()
                != original_query.lower()
            ):

                search_query = (
                    f"{last_user}\n"
                    f"{retrieval_query}"
                )

        docs = self.retrieve(
            search_query,
            k=5,
        )

        logger.info(
            "Retrieved %d documents",
            len(docs),
        )

        if len(docs) < 2:

            answer = (
                "I couldn't find enough verified legal "
                "information to answer this confidently. "
                "Please provide more details or consult "
                "a qualified advocate."
            )

            if language in ["hi", "hinglish"]:

                answer = translate_from_english(
                    answer,
                    language,
                )

            return {
                "answer": answer,
                "documents": docs,
                "sources": [],
                "language": language,
                "original_query": original_query,
            }

        if not docs:

            answer = (
                "The provided legal documents do not "
                "contain enough information."
            )

            if language in ["hi", "hinglish"]:

                answer = translate_from_english(
                    answer,
                    language,
                )

            self.memory.add(
                "user",
                original_query,
            )

            self.memory.add(
                "assistant",
                answer,
            )

            return {
                "answer": answer,
                "documents": [],
                "sources": [],
                "language": language,
                "original_query": original_query,
            }
        prompt = build_prompt(
            query=original_query,
            documents=docs,
            history=history,
        )

        logger.debug(
            "Prompt generated successfully."
        )

        answer = generate_response(
            prompt
        )

        if not answer:

            answer = (
                "Unable to generate a response."
            )

        # -----------------------------
        # Add citations
        # -----------------------------
        citation = "\n\n### Sources\n"

        for i, doc in enumerate(docs[:3], start=1):

            act = doc.metadata.get(
                "act",
                "Unknown Act",
            )

            section = doc.metadata.get(
                "section",
                "-",
            )

            page = doc.metadata.get(
                "page",
                "-",
            )

            source = doc.metadata.get(
                "source",
                "Unknown",
            )

            citation += (
                f"{i}. {act}\n"
                f"   Section: {section}\n"
                f"   Page: {page}\n"
                f"   File: {source}\n\n"
            )

        answer += citation

        # -----------------------------
        # Mandatory Disclaimer
        # -----------------------------
        answer += """

--------------------------------------------------

Disclaimer:
This response is generated from retrieved legal
documents and is intended only for general legal
information. It is not legal advice. Please consult
a qualified advocate for case-specific guidance.
"""

        # -----------------------------
        # Translate if required
        # -----------------------------
        if language in ["hi", "hinglish"]:

            answer = translate_from_english(
                answer,
                language,
            )
        # -----------------------------
        # Save Conversation Memory
        # -----------------------------
        self.memory.add(
            "user",
            original_query,
        )

        self.memory.add(
            "assistant",
            answer,
        )

        # -----------------------------
        # Build Source List
        # -----------------------------
        sources = []

        seen = set()

        for doc in docs:

            source = {
                "source": doc.metadata.get(
                    "source",
                    "Unknown Document",
                ),
                "page": doc.metadata.get(
                    "page",
                    "-",
                ),
                "section": doc.metadata.get(
                    "section",
                    "-",
                ),
                "act": doc.metadata.get(
                    "act",
                    "Unknown Act",
                ),
            }

            key = (
                source["source"],
                source["page"],
                source["section"],
            )

            if key not in seen:

                seen.add(key)

                sources.append(source)

        logger.info(
            "Generated answer successfully."
        )

        return {
            "answer": answer,
            "documents": docs,
            "sources": sources,
            "language": language,
            "original_query": original_query,
        }