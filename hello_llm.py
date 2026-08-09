import os

from openai import OpenAI


client = OpenAI(
    base_url="https://api.anthropic.com/v1/",
    api_key=os.environ["ANTHROPIC_API_KEY"],
)

response = client.chat.completions.create(
    model="claude-haiku-4-5",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one sentence.",
        }
    ],
)

print(response.choices[0].message.content)