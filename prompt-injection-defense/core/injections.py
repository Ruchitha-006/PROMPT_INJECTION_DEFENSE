import re

PATTERNS = [
    r"ignore previous instructions",
    r"act as .*",
    r"reveal .*",
    r"jailbreak",
]

def detect_injection(text):
    found = []

    for pattern in PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            found.append(pattern)

    return {
        "is_injection": len(found) > 0,
        "patterns": found
    }