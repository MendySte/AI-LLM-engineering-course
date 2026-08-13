from transformers import pipeline


MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"


generator = pipeline(
    "text-generation",
    model=MODEL_NAME,
)


prompt = """
You are a BI developer assistant.

Explain in simple terms:
What is a star schema and why is it useful in business intelligence?
"""


response = generator(
    prompt,
    max_new_tokens=200,
    do_sample=False,
    return_full_text=False,
)


print(response[0]["generated_text"])