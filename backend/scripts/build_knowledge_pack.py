import json
import re
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

RAW_DIR = Path("data/raw")
OUTPUT_DIR = Path("knowledge")

OUTPUT_DIR.mkdir(exist_ok=True)


SECTION_PATTERN = re.compile(
    r"(Section\s+\d+[A-Za-z\-]*|SECTION\s+\d+[A-Za-z\-]*)"
)


def detect_act_name(filename: str):
    """
    Detect act name from PDF filename.
    """

    name = filename.lower()

    if "bnss" in name:
        return "Bharatiya Nagarik Suraksha Sanhita, 2023"

    if "bns" in name:
        return "Bharatiya Nyaya Sanhita, 2023"

    if "rti" in name:
        return "Right to Information Act, 2005"

    if "consumer" in name:
        return "Consumer Protection Act, 2019"

    if "constitution" in name:
        return "Constitution of India"

    return filename


def split_sections(text: str):
    """
    Split legal text into logical sections.

    Supports:
    - Section 173
    - SECTION 173
    - SEC. 173
    - 173.
    - Article 14
    - ARTICLE 14
    - CHAPTER I
    - PART II
    """

    pattern = re.compile(
        r"(?=(?:Section\s+\d+[A-Za-z\-]*|"
        r"SECTION\s+\d+[A-Za-z\-]*|"
        r"SEC\.\s*\d+[A-Za-z\-]*|"
        r"Article\s+\d+[A-Za-z\-]*|"
        r"ARTICLE\s+\d+[A-Za-z\-]*|"
        r"CHAPTER\s+[IVXLC]+|"
        r"PART\s+[IVXLC]+|"
        r"^\d+\.\s))",
        re.MULTILINE,
    )

    sections = [
        s.strip()
        for s in pattern.split(text)
        if s.strip()
    ]

    return sections if sections else [text]
def build_entries():

    for pdf_file in sorted(RAW_DIR.glob("*.pdf")):

        print(f"\nProcessing {pdf_file.name}")

        loader = PyPDFLoader(str(pdf_file))

        pages = loader.load()

        act_name = detect_act_name(pdf_file.stem)

        entries = []

        counter = 1

        for page in pages:

            page_no = page.metadata.get("page", 0) + 1

            sections = split_sections(page.page_content)

            for section in sections:

                section = section.strip()

                if len(section) < 80:
                    continue

                match = SECTION_PATTERN.search(section)

                section_name = ""

                if match:
                    section_name = match.group(0)

                title = section_name if section_name else f"Page {page_no}"

                search_text = (
                    f"{act_name} "
                    f"{section_name} "
                    f"{section}"
                )

                entry = {

                    "id": f"{pdf_file.stem.upper()}-{counter:05}",

                    "domain": "Legal",

                    "category": act_name,

                    "subcategory": section_name,

                    "act": act_name,

                    "section": section_name,

                    "old_law_reference": {
                        "act": "",
                        "section": ""
                    },

                    "applicable_to": [],

                    "jurisdiction": "India",

                    "severity": "informational",

                    "urgency": "normal",

                    "intent": [
                        "definition"
                    ],

                    "keywords": [],

                    "search_text": search_text,

                    "translations": {

                        "en": {

                            "title": title,

                            "content": section,

                            "steps": [],

                            "documents_required": []

                        },

                        "hi": {

                            "title": "",

                            "content": "",

                            "steps": [],

                            "documents_required": []

                        },

                        "hinglish": {

                            "title": "",

                            "content": "",

                            "steps": [],

                            "documents_required": []

                        }

                    },

                    "related_ids": [],

                    "source": pdf_file.name,

                    "source_url": "",

                    "disclaimer": "General legal information only.",

                    "last_verified": "2026-07-01",

                    "version": 1

                }

                entries.append(entry)

                counter += 1

        output = OUTPUT_DIR / f"{pdf_file.stem}.json"

        with open(output, "w", encoding="utf-8") as f:

            json.dump(
                entries,
                f,
                indent=2,
                ensure_ascii=False,
            )

        print(
            f"Saved {len(entries)} entries -> {output.name}"
        )


if __name__ == "__main__":

    build_entries()