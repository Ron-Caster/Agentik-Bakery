from pathlib import Path
from models.providers.groq_models import call_groq, extract_text
import json

PROMPT_PATH = Path(__file__).with_name("PROMPT.md")
PROMPT_TEMPLATE = PROMPT_PATH.read_text(encoding="utf-8").strip()


def intent_json(user_input: str) -> dict:
    prompt = PROMPT_TEMPLATE.replace("{input}", user_input)
    response = call_groq(prompt)
    raw_text = extract_text(response).strip()
    return json.loads(raw_text)
