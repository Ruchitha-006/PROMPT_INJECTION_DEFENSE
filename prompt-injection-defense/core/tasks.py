def sanitize_text(text):
    dangerous_phrases = [
        "ignore previous instructions",
        "act as",
        "reveal",
        "jailbreak"
    ]

    clean = text
    for phrase in dangerous_phrases:
        clean = clean.replace(phrase, "")

    return clean