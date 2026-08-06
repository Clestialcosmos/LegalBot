import re

from langdetect import detect


HINGLISH_WORDS = {
    "mujhe", "mera", "meri", "mere",
    "kya", "kaise", "kyun", "kab",
    "hai", "hain", "ho", "tha", "thi",
    "batao", "samjhao", "madad",
    "nahi", "haan", "aur", "agar",
    "karo", "karna", "kar", "sakta", "sakti"
}


def detect_language(text: str) -> str:
    """
    Detect English, Hindi and Hinglish.
    """

    text = text.strip().lower()

    # Hindi (Devanagari)
    if re.search(r"[\u0900-\u097F]", text):
        return "hi"

    # Hinglish
    words = set(text.split())

    if len(words.intersection(HINGLISH_WORDS)) >= 2:
        return "hinglish"

    # English / Other
    try:
        return detect(text)
    except Exception:
        return "en"