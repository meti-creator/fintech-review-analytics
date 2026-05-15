import spacy
import re

# Load the spaCy model once
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def clean_text(text, lemmatize=True, remove_stop=True):
    """
    Handles: Tokenization, Noise Removal, Stop-word removal, and Lemmatization.
    """
    if not isinstance(text, str):
        return ""

    # 1. Noise Removal: Remove special characters/numbers & lowercase
    # This leaves only letters and spaces
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())

    # 2. Process with spaCy (Tokenization happens here automatically)
    doc = nlp(text)

    # 3. Filtering and Lemmatization
    tokens = []
    for token in doc:
        # Check if it's a stop-word (e.g., 'the', 'is', 'and')
        is_stop = remove_stop and token.is_stop
        
        if not is_stop and not token.is_space:
            # Use lemma (root word) if requested, else use raw text
            val = token.lemma_ if lemmatize else token.text
            tokens.append(val)

    return " ".join(tokens)
