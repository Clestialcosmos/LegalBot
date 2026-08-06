FOLLOW_UP_WORDS = {
    "it",
    "this",
    "that",
    "they",
    "them",
    "he",
    "she",
    "its",
    "explain",
    "why",
    "how",
    "when",
    "where",
    "who",
    "conditions",
    "cancel",
    "cancelled",
    "eligibility",
}
EMERGENCY_KEYWORDS = {
    # Violence
    "kill",
    "kill me",
    "trying to kill",
    "murder",
    "attack",
    "assault",
    "domestic violence",
    "rape",
    "molestation",
    "kidnapping",
    "human trafficking",
    "child abuse",
    "acid attack",

    # Self-harm
    "suicide",
    "kill myself",
    "self harm",

    # Cyber
    "cyber fraud",
    "bank fraud",
    "hacked",
    "hack",
    "scam",

    # Hindi
    "हत्या",
    "मार डाल",
    "आत्महत्या",
    "घरेलू हिंसा",
    "बलात्कार",
    "अपहरण",
    "साइबर धोखाधड़ी",

    # Hinglish
    "maar denge",
    "kill kar",
    "aatmahatya",
    "gharelu hinsa",
    "kidnap",
}


LEGAL_KEYWORDS = {

    # English
    "law",
    "legal",
    "court",
    "judge",
    "bail",
    "police",
    "fir",
    "contract",
    "consumer",
    "constitution",
    "ipc",
    "bns",
    "bnss",
    "evidence",
    "rti",
    "cyber",
    "advocate",
    "lawyer",
    "crime",
    "arrest",
    "article",
    "article 14",
    "article 19",
    "article 21",
    "fundamental rights",
    "fundamental duty",
    "directive principles",
    "preamble",
    "constitution of india",
    "writ",
    "habeas corpus",
    "mandamus",
    "certiorari",
    "quo warranto",
    "prohibition"

    # Hindi
    "कानून",
    "अदालत",
    "न्यायालय",
    "जमानत",
    "अग्रिम जमानत",
    "पुलिस",
    "एफआईआर",
    "संविधान",
    "उपभोक्ता",
    "आरटीआई",
    "गिरफ्तारी",
    "वकील",
    "अपराध",

    # Hinglish
    "kanoon",
    "jamanat",
    "agrim jamanat",
    "court",
    "police",
    "fir",
    "vakil",
    "lawyer",
    "rti",
    "consumer court",
    "arrest",
    "crime",
}


def emergency_response():
    return {
        "emergency": True,
        "answer": (
            "This appears to be an emergency.\n\n"
            "Please contact the appropriate emergency services immediately.\n\n"
            "India Emergency Number: 112\n"
            "Women Helpline: 181\n"
            "Cyber Crime: 1930\n\n"
            "LegalBot cannot replace professional legal or emergency assistance."
        ),
    }


def check_emergency(query: str):
    q = query.lower()

    return emergency_response() if any(word in q for word in EMERGENCY_KEYWORDS) else None


def is_legal_query(query: str):
    q = query.lower()

    print("Checking query:", q)

    for word in LEGAL_KEYWORDS:
        if word in q:
            print("Matched keyword:", word)
            return True

    print("No legal keyword matched")
    return False