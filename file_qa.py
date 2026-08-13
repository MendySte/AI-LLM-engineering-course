import os
import sys

from openai import OpenAI


NOT_FOUND_MESSAGE = "I can't find that in the document."


def load_document(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def ask_document(document_text: str, question: str) -> str:
    client = OpenAI(
        base_url="https://api.anthropic.com/v1/",
        api_key=os.environ["ANTHROPIC_API_KEY"],
    )

    system_prompt = f"""
You are a grounded BI, Qlik and SQL assistant.

Rules:
1. Answer ONLY using the provided document.
2. Do not use outside knowledge.
3. Do not guess.
4. If the answer is not explicitly supported by the document, reply exactly:
{NOT_FOUND_MESSAGE}
5. If you can answer, use exactly this format:

Answer: <concise answer>

Reference: "<one exact continuous passage copied verbatim from the document>"

6. The Reference must be copied word-for-word from the document.
7. Do not paraphrase the Reference.
8. Do not use ellipsis (...) inside the Reference.
9. Use one continuous passage only.
"""

    user_prompt = f"""
DOCUMENT:
{document_text}

QUESTION:
{question}
"""

    response = client.chat.completions.create(
        model="claude-haiku-4-5",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        temperature=0,
        max_tokens=500,
    )

    answer = response.choices[0].message.content

    if answer is None:
        raise ValueError("The model returned an empty response.")

    answer = answer.strip()

    if answer.startswith(NOT_FOUND_MESSAGE):
        return NOT_FOUND_MESSAGE

    return answer


def main():
    if len(sys.argv) < 3:
        print('Usage: python file_qa.py <file_path> "<question>"')
        sys.exit(1)

    file_path = sys.argv[1]
    question = sys.argv[2]

    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)

    document_text = load_document(file_path)
    answer = ask_document(document_text, question)

    print(answer)


if __name__ == "__main__":
    main()
        