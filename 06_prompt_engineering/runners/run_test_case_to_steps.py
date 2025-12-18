from openai import OpenAI
import json

client = OpenAI()  # uses OPENAI_API_KEY automatically

PROMPT_FILE = "../structured_prompts/test_case_to_steps.json"

with open(PROMPT_FILE) as f:
    prompt_payload = json.load(f)

response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": prompt_payload["role"]},
        {"role": "user", "content": json.dumps(prompt_payload, indent=2)}
    ]
)

print(response.output_text)
