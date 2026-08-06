from app.ai.groq_client import generate_response


def translate_to_english(text: str):
    prompt = f"""
Translate the following text into English.

Only return the translation.

{text}
"""

    return generate_response(prompt)


def translate_from_english(text: str, language: str):
    prompt = f"""
Translate the following English text into {language}.

Only return the translation.

{text}
"""

    return generate_response(prompt)