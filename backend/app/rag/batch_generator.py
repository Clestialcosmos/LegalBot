import json
import logging
import os
import time

from dotenv import load_dotenv
from groq import Groq
from json_repair import repair_json

load_dotenv()

logger = logging.getLogger(__name__)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
You are an Indian legal knowledge generator.

Return ONLY valid JSON.

No markdown.

Return JSON array.

Each section becomes ONE object.

Schema:

[
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
]
"""


def generate_batch(
    act_name,
    sections,
    retries=3,
):

    prompt = f"Act:\n{act_name}\n\n"

    for i, section in enumerate(sections):

        prompt += f"""
========================
SECTION {i+1}

Title:
{section["section"]}

Content:

{section["content"]}

"""

    for attempt in range(retries):

        try:

            response = client.chat.completions.create(

                model="llama-3.3-70b-versatile",

                temperature=0.1,

                response_format={
                    "type": "json_object"
                },

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

            text = response.choices[0].message.content

            text = (
                text.replace("```json", "")
                .replace("```", "")
                .strip()
            )

            text = repair_json(text)

            data = json.loads(text)

            if isinstance(data, dict):

                if "entries" in data:
                    return data["entries"]

                if "data" in data:
                    return data["data"]

            return data

        except Exception as exc:

            logger.exception(exc)

            print(
                f"Retry {attempt+1}/{retries}"
            )

            time.sleep(2)

    raise RuntimeError(
        "Groq failed after retries."
    )