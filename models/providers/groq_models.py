# GROQ
# available models:
# llama-3.1-8b-instant
# llama-3.3-70b-versatile
# openai/gpt-oss-120b
# openai/gpt-oss-20b
# meta-llama/llama-4-scout-17b-16e-instruct
# qwen/qwen3-32b

import json
import os
from urllib.request import Request, urlopen

MODEL = "llama-3.1-8b-instant"
ENDPOINT = "https://api.groq.com/openai/v1/responses"


def call_groq(prompt: str) -> dict:
    api_key = os.environ["GROQ_API_KEY"]

    payload = json.dumps({"model": MODEL, "input": prompt}).encode("utf-8")
    request = Request(ENDPOINT, data=payload, headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Python urllib",
    }, method="POST")

    with urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def extract_text(response: dict) -> str:
    if not isinstance(response, dict):
        raise ValueError("Invalid Groq response")

    output = response.get("output")
    if not isinstance(output, list) or not output:
        raise ValueError("Unable to extract text from Groq response")

    for item in output:
        if not isinstance(item, dict):
            continue
        content = item.get("content")
        if not isinstance(content, list):
            continue
        for entry in content:
            if not isinstance(entry, dict):
                continue
            if entry.get("type") == "output_text" and isinstance(entry.get("text"), str):
                return entry["text"]

    for item in output:
        if not isinstance(item, dict):
            continue
        content = item.get("content")
        if not isinstance(content, list):
            continue
        for entry in content:
            if not isinstance(entry, dict):
                continue
            if isinstance(entry.get("text"), str):
                return entry["text"]

    first = output[0]
    if isinstance(first, dict):
        text = first.get("text")
        if isinstance(text, str):
            return text

    raise ValueError("Unable to extract text from Groq response")


