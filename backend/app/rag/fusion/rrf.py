from collections import defaultdict
import logging

from langchain_core.documents import Document

logger = logging.getLogger(__name__)


def _document_key(doc: Document):
    """
    Generate a stable unique key for a document.
    """

    return (
        doc.metadata.get("source", ""),
        doc.metadata.get("page", -1),
        hash(doc.page_content),
    )


def reciprocal_rank_fusion(
    faiss_docs: list[Document],
    bm25_docs: list[Document],
    k: int = 60,
):
    """
    Reciprocal Rank Fusion (RRF)

    Combines ranked results from multiple retrievers.

    Parameters
    ----------
    faiss_docs : list[Document]
    bm25_docs : list[Document]
    k : int
        RRF constant (default = 60)

    Returns
    -------
    list[Document]
        Fused and reranked unique documents.
    """

    fused_scores = defaultdict(float)
    fused_docs = {}

    retrievers = [
        faiss_docs,
        bm25_docs,
    ]

    for results in retrievers:

        for rank, doc in enumerate(results):

            key = _document_key(doc)

            fused_scores[key] += 1.0 / (k + rank + 1)

            if key not in fused_docs:
                fused_docs[key] = doc

    ranked_keys = sorted(
        fused_scores.keys(),
        key=lambda key: fused_scores[key],
        reverse=True,
    )

    ranked_docs = [
        fused_docs[key]
        for key in ranked_keys
    ]

    logger.info(
        "RRF fused %d unique documents.",
        len(ranked_docs),
    )

    return ranked_docs