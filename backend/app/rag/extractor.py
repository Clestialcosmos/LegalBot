import re
import logging
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

logger = logging.getLogger(__name__)

# Matches:
# Section 1
# Section 1A
# Section 173
# Section 173(1)
SECTION_PATTERN = re.compile(
    r"(Section\s+\d+[A-Za-z]?(?:\([^)]+\))?)",
    flags=re.IGNORECASE,
)


def load_pdf(pdf_path: str) -> str:
    """
    Load an entire PDF into a single string.
    """

    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"{pdf_path} not found")

    loader = PyPDFLoader(str(pdf_path))

    pages = loader.load()

    text = "\n".join(page.page_content for page in pages)

    logger.info(
        "Loaded %d pages from %s",
        len(pages),
        pdf_path.name,
    )

    return text


def extract_sections(text: str):
    """
    Split a legal Act into sections.

    Returns:
        [
            {
                "section": "...",
                "content": "..."
            }
        ]
    """

    matches = list(SECTION_PATTERN.finditer(text))

    if not matches:

        logger.warning("No sections found.")

        return [
            {
                "section": "Full Document",
                "content": text.strip(),
            }
        ]

    sections = []

    for i, match in enumerate(matches):

        start = match.start()

        end = (
            matches[i + 1].start()
            if i + 1 < len(matches)
            else len(text)
        )

        section_title = match.group().strip()

        section_text = text[start:end].strip()

        sections.append(
            {
                "section": section_title,
                "content": section_text,
            }
        )

    logger.info(
        "Extracted %d sections.",
        len(sections),
    )

    return sections


def extract_pdf(pdf_path: str):
    """
    Complete extraction pipeline.

    PDF
        ↓
    Text
        ↓
    Sections
    """

    text = load_pdf(pdf_path)

    return extract_sections(text)