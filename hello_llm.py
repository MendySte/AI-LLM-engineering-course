import json
import os

from openai import OpenAI
from pydantic import BaseModel, Field


class Answer(BaseModel):
    answer: str
    confidence: float = Field(ge=0, le=1)


def remove_json_code_fence(response_text: str) -> str:
    """Remove optional Markdown code fences from a JSON response."""

    cleaned_text = response_text.strip()

    if cleaned_text.startswith("```"):
        lines = cleaned_text.splitlines()

        # Remove the opening ``` or ```json line.
        lines = lines[1:]

        # Remove the closing ``` line.
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        cleaned_text = "\n".join(lines).strip()

    return cleaned_text


SYSTEM_PROMPT = """
You are a senior business intelligence developer.

Return one valid JSON object only.
Do not use Markdown.
Do not use code fences.
Do not add text before or after the JSON.

Your entire response must start with { and end with }.

Use exactly this structure:
{
  "answer": "Your concise answer",
  "confidence": 0.95
}

The answer must be a string.
The confidence must be a number between 0 and 1.
"""

USER_PROMPT = """
What is the purpose of a star schema in business intelligence?
"""


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
    temperature=0,
    max_tokens=300,
)

response_text = response.choices[0].message.content

if response_text is None:
    raise ValueError("The model returned an empty response.")

cleaned_json = remove_json_code_fence(response_text)


print("Raw model response:")
print(response_text)


# Method 1: Parse with Python's built-in json module.
json_data = json.loads(cleaned_json)

print("\nParsed with json:")
print(f"Answer: {json_data['answer']}")
print(f"Confidence: {json_data['confidence']}")


# Method 2: Parse and validate with Pydantic.
validated_answer = Answer.model_validate_json(cleaned_json)

print("\nValidated with Pydantic:")
print(f"Answer: {validated_answer.answer}")
print(f"Confidence: {validated_answer.confidence}")


print(type(response_text))
print(type(json_data))
print(type(validated_answer))
print(f"Response text: {response_text}")

