from openai import OpenAI
import json
import os
from pathlib import Path

# Initialize OpenAI client (reads OPENAI_API_KEY automatically)
client = OpenAI()

# Resolve prompt file path safely
BASE_DIR = Path(__file__).resolve().parent
PROMPT_FILE = BASE_DIR / "../structured_prompts/logs_to_root_cause.json"

# Load prompt payload
with open(PROMPT_FILE, "r") as f:
    prompt_payload = json.load(f)

# Build messages
messages = [
    {
        "role": "system",
        "content": prompt_payload["role"]
    },
    {
        "role": "user",
        "content": json.dumps(prompt_payload, indent=2)
    }
]

# Call OpenAI
response = client.responses.create(
    model="gpt-5-mini",
    input=messages
)

# Print structured output
print("\n===== INCIDENT ANALYSIS OUTPUT =====\n")
print(response.output_text)
print("\n====================================\n")
