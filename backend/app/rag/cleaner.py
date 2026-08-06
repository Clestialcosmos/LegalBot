import re


def clean_text(text: str) -> str:
    """
    Clean raw legal text extracted from PDFs.
    """

    if not text:
        return ""

    # Normalize newlines
    text = text.replace("\r", "\n")

    # Remove page numbers like:
    # Page 12
    # 12
    # - 12 -
    text = re.sub(r"\bPage\s+\d+\b", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"^\s*\d+\s*$", " ", text, flags=re.MULTILINE)
    text = re.sub(r"-\s*\d+\s*-", " ", text)

    # Remove repeated Government headers
    patterns = [
        r"Government of India",
        r"भारत सरकार",
        r"MINISTRY OF.*",
        r"Ministry of.*",
        r"Gazette of India.*",
        r"Extraordinary.*",
    ]

    for pattern in patterns:
        text = re.sub(
            pattern,
            " ",
            text,
            flags=re.IGNORECASE,
        )

    # Remove excessive whitespace
    text = re.sub(r"\n{2,}", "\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)

    # Merge broken lines
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)

    # Remove spaces before punctuation
    text = re.sub(r"\s+([.,;:])", r"\1", text)

    return text.strip()


def clean_section(section: dict) -> dict:
    """
    Clean one extracted section.
    """

    return {
        "section": section["section"],
        "content": clean_text(section["content"]),
    }


def clean_sections(sections: list[dict]) -> list[dict]:
    """
    Clean all extracted sections.
    """

    cleaned = []

    for section in sections:
        cleaned.append(
            clean_section(section)
        )

    return cleaned