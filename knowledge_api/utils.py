import json
from pathlib import Path
import difflib

BASE_DIR = Path(__file__).resolve().parent
KB_PATH = BASE_DIR / "data" / "kb_chunks.json"

def load_chunks():
    with open(KB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def find_relevant_chunk(query, chunks):
    topics = [chunk["topic"] for chunk in chunks]
    match = difflib.get_close_matches(query.lower(), topics, n=1)
    if match:
        return next((c for c in chunks if c["topic"] == match[0]), None)
    return None
