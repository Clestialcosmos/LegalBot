import json
import logging
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

logger = logging.getLogger(__name__)

RAW_DATA_DIR = Path("data/raw")
KNOWLEDGE_DIR = Path("knowledge")


def load_pdf_documents() -> list[Document]:
    """
    Load all legal PDFs.
    """

    documents = []

    pdf_files = sorted(RAW_DATA_DIR.glob("*.pdf"))

    if not pdf_files:

        logger.warning(
            "No PDF files found."
        )

        return documents

    for pdf in pdf_files:

        logger.info(
            "Loading PDF: %s",
            pdf.name,
        )

        loader = PyPDFLoader(str(pdf))

        docs = loader.load()

        for doc in docs:

            doc.metadata["source"] = pdf.name

        documents.extend(docs)

    logger.info(
        "Loaded %d PDF pages.",
        len(documents),
    )

    return documents


def load_knowledge_documents() -> list[Document]:
    """
    Load curated knowledge packs.
    """

    documents = []

    json_files = sorted(
        KNOWLEDGE_DIR.glob("*.json")
    )

    if not json_files:

        logger.warning(
            "No knowledge packs found."
        )

        return documents

    for file in json_files:

        logger.info(
            "Loading Knowledge Pack: %s",
            file.name,
        )

        with open(
            file,
            encoding="utf-8",
        ) as f:

            entries = json.load(f)

        for entry in entries:

            translations = entry.get(
                "translations",
                {},
            )

            hindi = translations.get(
                "hi",
                {},
            )

            text = "\n".join(
                [

                    entry.get(
                        "question",
                        "",
                    ),

                    entry.get(
                        "answer",
                        "",
                    ),

                    hindi.get(
                        "title",
                        "",
                    ),

                    hindi.get(
                        "summary",
                        "",
                    ),

                    entry.get(
                        "search_text",
                        "",
                    ),

                    " ".join(
                        entry.get(
                            "keywords",
                            [],
                        )
                    ),
                ]
            )

            metadata = {

                "id": entry.get(
                    "id",
                ),

                "domain": entry.get(
                    "domain",
                ),

                "category": entry.get(
                    "category",
                ),

                "subcategory": entry.get(
                    "subcategory",
                ),

                "act": entry.get(
                    "act",
                ),

                "section": entry.get(
                    "section",
                ),

                "jurisdiction": entry.get(
                    "jurisdiction",
                ),

                "source": file.name,

                "language": "en",

                "version": entry.get(
                    "version",
                ),

                "last_verified": entry.get(
                    "last_verified",
                ),

                "keywords": ", ".join(
                    entry.get(
                        "keywords",
                        [],
                    )
                ),
            }

            documents.append(

                Document(

                    page_content=text,

                    metadata=metadata,

                )

            )

    logger.info(

        "Loaded %d knowledge entries.",

        len(documents),

    )

    return documents


def load_documents():
    """
    Load complete LegalBot knowledge base.
    """

    pdf_docs = load_pdf_documents()

    knowledge_docs = load_knowledge_documents()

    documents = pdf_docs + knowledge_docs

    logger.info(

        "Total documents loaded: %d",

        len(documents),

    )

    return documents