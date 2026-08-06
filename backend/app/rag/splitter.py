import logging
import re

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

logger = logging.getLogger(__name__)

SECTION_PATTERN = re.compile(
    r"(Section\s+\d+[A-Za-z\-]*|"
    r"SECTION\s+\d+[A-Za-z\-]*|"
    r"SEC\.\s*\d+[A-Za-z\-]*|"
    r"Article\s+\d+[A-Za-z\-]*|"
    r"ARTICLE\s+\d+[A-Za-z\-]*|"
    r"CHAPTER\s+[IVXLC]+|"
    r"PART\s+[IVXLC]+)",
    re.IGNORECASE,
)


def split_documents(
    documents: list[Document],
) -> list[Document]:
    """
    Split PDF documents into chunks.

    Knowledge Pack entries are already curated,
    so they are NOT split.
    """

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=1000,

        chunk_overlap=200,

        separators=[
            "\n\n",
            "\n",
            ". ",
            ";",
            ",",
            " ",
            "",
        ],
    )

    chunks = []

    for doc in documents:

        source = str(
            doc.metadata.get(
                "source",
                "",
            )
        ).lower()

        # -----------------------------
        # Knowledge Packs
        # -----------------------------

        if source.endswith(".json"):

            chunks.append(doc)

            continue

        # -----------------------------
        # PDFs
        # -----------------------------

        pdf_chunks = splitter.split_documents(
            [doc]
        )

        for chunk in pdf_chunks:

            text = chunk.page_content

            match = SECTION_PATTERN.search(
                text
            )

            if match:

                chunk.metadata[
                    "section"
                ] = match.group(0)

            chunks.append(chunk)

    logger.info(

        "Created %d chunks.",

        len(chunks),

    )

    return chunks