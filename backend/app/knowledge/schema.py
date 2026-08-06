from pydantic import BaseModel, Field
from typing import List


class Translation(BaseModel):
    title: str = ""
    content: str = ""
    steps: List[str] = Field(default_factory=list)
    documents_required: List[str] = Field(default_factory=list)


class OldLawReference(BaseModel):
    act: str = ""
    section: str = ""


class KnowledgeEntry(BaseModel):
    id: str

    domain: str

    category: str

    subcategory: str

    act: str

    section: str

    old_law_reference: OldLawReference

    applicable_to: List[str]

    jurisdiction: str = "India"

    severity: str = "informational"

    urgency: str = "normal"

    intent: List[str]

    keywords: List[str]

    search_text: str

    translations: dict

    related_ids: List[str]

    source: str

    source_url: str = ""

    disclaimer: str = "General legal information only."

    last_verified: str = "2026-07-01"

    version: int = 1