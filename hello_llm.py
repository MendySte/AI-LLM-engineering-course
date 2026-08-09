import os

from openai import OpenAI


def main() -> None:
    """Send a simple prompt to OpenAI and print the response."""

    client = OpenAI(
        api_key=os.environ["OPENAI_API_KEY"],
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": "Say hello in one sentence.",
            }
        ],
        max_tokens=50,
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
