import re

from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


SECTION_PATTERN = re.compile(
    r"(Section\s+\d+[A-Za-z\-]*)",
    flags=re.IGNORECASE,
)


def load_pdf(pdf_path: str):

    loader = PyPDFLoader(pdf_path)

    docs = loader.load()

    text = "\n".join(
        page.page_content
        for page in docs
    )

    return text


def extract_sections(text: str):

    matches = list(
        SECTION_PATTERN.finditer(text)
    )

    if not matches:

        return [
            {
                "section": "Full Document",
                "content": text,
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

        section = match.group()

        body = text[start:end].strip()

        sections.append(
            {
                "section": section,
                "content": body,
            }
        )

    return sections


def extract_pdf(pdf_path):

    text = load_pdf(pdf_path)

    return extract_sections(text)