from app.rag.extractor import extract_pdf

sections = extract_pdf(
    "data/raw/RTI_Act_2005.pdf"
)

print("Sections:", len(sections))
print()

print(sections[0]["section"])
print()

print(sections[0]["content"][:1000])