import logging
import re

from langchain_core.documents import Document
from rank_bm25 import BM25Okapi

logger = logging.getLogger(__name__)


class BM25Retriever:
    """
    Keyword-based BM25 Retriever.
    """

    def __init__(
        self,
        documents: list[Document],
    ):

        if not documents:

            raise ValueError(
                "No documents supplied to BM25."
            )

        self.documents = documents

        self.tokenized_docs = [

            self.tokenize(
                doc.page_content
            )

            for doc in documents

        ]

        self.bm25 = BM25Okapi(
            self.tokenized_docs
        )

        logger.info(
            "BM25 initialized with %d documents.",
            len(documents),
        )

    @staticmethod
    def tokenize(
        text: str,
    ) -> list[str]:
        """
        Tokenize text.
        """

        return re.findall(
            r"\w+",
            text.lower(),
        )

    def search(
        self,
        query: str,
        k: int = 5,
    ):
        """
        Return top-k BM25 documents.
        """

        if not query.strip():

            return []

        query_tokens = self.tokenize(
            query
        )

        scores = self.bm25.get_scores(
            query_tokens
        )

        ranked = sorted(

            zip(
                scores,
                self.documents,
            ),

            key=lambda item: item[0],

            reverse=True,

        )

        documents = [

            doc

            for score, doc in ranked

            if score > 0

        ]

        logger.info(

            "BM25 returned %d documents.",

            len(documents[:k]),

        )

        return documents[:k]