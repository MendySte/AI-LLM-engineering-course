import os

from openai import OpenAI


SYSTEM_PROMPT = """
You are a senior Qlik Sense developer.
Answer in clear and simple English.
Do not use Markdown headings.
Include valid Qlik syntax when relevant.
"""

USER_PROMPT = """
Explain the difference between inner and outer set expressions.
"""

TEMPERATURE = 1
MAX_TOKENS = 300


client = OpenAI(
    base_url="https://api.anthropic.com/v1/",
    api_key=os.environ["ANTHROPIC_API_KEY"],
)

response = client.chat.completions.create(
    model="claude-haiku-4-5",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": USER_PROMPT,
        },
    ],
    temperature=TEMPERATURE,
    max_tokens=MAX_TOKENS,
)

print(response.choices[0].message.content)