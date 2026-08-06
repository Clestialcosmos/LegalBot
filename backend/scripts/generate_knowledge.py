from pathlib import Path

from app.rag.extractor import extract_pdf
from app.rag.cleaner import clean_sections
from app.rag.batch_generator import generate_batch
from app.rag.writer import KnowledgeWriter
from app.rag.validator import validate_entry
from app.rag.utils import chunks

RAW_DIR = Path("data/raw")

writer = KnowledgeWriter()

for pdf in RAW_DIR.glob("*.pdf"):

    print("=" * 60)
    print(pdf.name)

    sections = extract_pdf(str(pdf))

    sections = clean_sections(sections)

    entries = []

    domain = pdf.stem.upper()

    counter = 1

    for batch in chunks(sections, 2):

        ai_entries = generate_batch(
            pdf.stem,
            batch,
        )

        for section, ai in zip(batch, ai_entries):

            ai["id"] = writer.generate_id(domain)

            ai["act"] = pdf.stem

            ai["section"] = section["section"]

            ai["old_law_reference"] = {
                "act": "",
                "section": "",
            }

            ai["applicable_to"] = []

            ai["jurisdiction"] = "India"

            ai["search_text"] = (
                pdf.stem
                + "\n"
                + section["section"]
                + "\n"
                + section["content"]
            )

            ai["related_ids"] = []

            ai["source"] = pdf.name

            ai["source_url"] = ""

            ai["disclaimer"] = (
                "General legal information only."
            )

            ai["last_verified"] = "2026-07-01"

            ai["version"] = 1

            validate_entry(ai)

            entries.append(ai)

            counter += 1

            print(ai["id"])

    writer.save(
        pdf.stem,
        entries,
    )