# Assignment 1 - Reflections

## Hosted LLM

I used Claude Haiku through the Anthropic API.

### Temperature

With temperature 0, the answers were more consistent between runs.

With temperature 1, the responses showed more variation in wording and structure.

For factual BI questions, I found temperature 0 more suitable because consistency is more important than creativity.

## Grounded Document Q&A

I created a document-based Q&A script that answers questions only from the provided document.

When the requested information was not available, the model was instructed to return:

"I can't find that in the document."

Providing the source document and requiring an exact reference reduced the model's ability to invent unsupported answers.

## Local Open-Source Model

I ran Qwen2.5-0.5B-Instruct locally using Hugging Face Transformers and PyTorch.

The model worked successfully on my local machine without an external inference API.

However, its answer about star schemas contained an important factual error: it claimed that a star schema is organized into three tables.

This demonstrated the difference between successfully running a model and receiving a reliable answer.

## Hosted vs Local

Claude produced a significantly better answer than the small local Qwen model.

The local model provides more control and can run without sending prompts to an external API, but model quality and local compute resources become important considerations.

For the BI assistant project, grounding and evaluation will be important, especially when using smaller local models.