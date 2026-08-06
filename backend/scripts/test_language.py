from app.services.language_service import detect_language

tests = [
    "What is anticipatory bail?",
    "मुझे अग्रिम जमानत के बारे में बताइए",
    "Mujhe anticipatory bail ke baare mein batao",
    "Kya consumer court mein complaint kar sakta hu?",
    "How to file an RTI?"
]

for text in tests:
    print(f"{text}")
    print(f"Detected: {detect_language(text)}")
    print("-" * 50)