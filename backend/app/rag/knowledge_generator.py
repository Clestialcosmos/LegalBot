import json
import logging
import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

logger = logging.getLogger(__name__)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
You are an Indian legal expert.

You are given ONE section of a law.

Return ONLY valid JSON.

Do NOT wrap in markdown.

Return ONLY this schema.

{
"domain":"",
"category":"",
"subcategory":"",
"severity":"",
"urgency":"",
"intent":[],
"keywords":[],
"translations":{
    "en":{
        "title":"",
        "content":"",
        "steps":[],
        "documents_required":[]
    },
    "hi":{
        "title":"",
        "content":"",
        "steps":[],
        "documents_required":[]
    },
    "hinglish":{
        "title":"",
        "content":"",
        "steps":[],
        "documents_required":[]
    }
}
}

Rules:

- Return JSON only.
- No explanation.
- No markdown.
- Keep content concise.
- Generate useful keywords.
- Hindi should be proper Hindi.
- Hinglish should be natural.
"""


def generate_metadata(
    act_name: str,
    section: str,
    content: str,
):
    """
    Generate only AI-required fields.
    """

    prompt = f"""
Act:
{act_name}

Section:
{section}

Text:
{content}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    text = response.choices[0].message.content.strip()

    if text.startswith("```"):
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

    return json.loads(text)


def build_entry(
    idx: int,
    act_name: str,
    source_file: str,
    section: str,
    content: str,
):
    """
    Build the final knowledge entry.
    """

    ai = generate_metadata(
        act_name,
        section,
        content,
    )

    prefix = (
        act_name.upper()
        .replace(" ", "_")
        .replace(",", "")
    )

    entry = {

        "id":
        f"{prefix}-{idx:05d}",

        "domain":
        ai["domain"],

        "category":
        ai["category"],

        "subcategory":
        ai["subcategory"],

        "act":
        act_name,

        "section":
        section,

        "old_law_reference": {
            "act": "",
            "section": ""
        },

        "applicable_to": [],

        "jurisdiction":
        "India",

        "severity":
        ai["severity"],

        "urgency":
        ai["urgency"],

        "intent":
        ai["intent"],

        "keywords":
        ai["keywords"],

        "search_text":
        f"{act_name}\n{section}\n{content}",

        "translations":
        ai["translations"],

        "related_ids": [],

        "source":
        source_file,

        "source_url": "",

        "disclaimer":
        "General legal information only.",

        "last_verified":
        "2026-07-01",

        "version":
        1,
    }

    return entry