# AI & LLM Engineering Course

A hands-on AI engineering project built throughout the AI & LLM Engineering course.

The project explores hosted and local language models, prompt engineering, structured outputs, grounded question answering, evaluation, and eventually RAG-based applications.

## Project Goal

The long-term goal is to build a **BI Developer Assistant** focused on:

- Qlik Sense and Qlik Cloud
- Business Intelligence
- SQL
- Data modeling
- Analytics development best practices

The assistant will gradually evolve throughout the course as new AI engineering concepts are introduced.

## Current Progress

### Hosted LLM

`hello_llm.py`

Uses Claude through Anthropic's OpenAI-compatible API.

Implemented:

- System and user prompts
- Temperature experiments
- Structured JSON output
- JSON parsing
- Pydantic validation
- Environment-based API key management

### Grounded Document Q&A

`file_qa.py`

Answers questions using only information contained in a supplied document.

Features:

- Loads a local knowledge document
- Accepts a question from the command line
- Prevents use of outside knowledge through prompting
- Returns an exact supporting reference
- Returns `I can't find that in the document.` when the answer is not supported

Example:

```powershell
python file_qa.py .\documents\bi\qlik_bi_notes.md "What is a star schema?"
```

### Local Open-Source LLM

`local_llm.py`

Runs:

```text
Qwen/Qwen2.5-0.5B-Instruct
```

locally using Hugging Face Transformers and PyTorch.

The model runs locally without sending inference requests to an external LLM API.

This also provides a baseline for comparing small local models with hosted models such as Claude.

## Project Structure

```text
AI-LLM-engineering-course/
│
├── hello_llm.py
├── file_qa.py
├── local_llm.py
├── reflections.md
├── requirements.txt
│
├── documents/
│   ├── qlik/
│   ├── sql/
│   └── bi/
│       └── qlik_bi_notes.md
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
├── outputs/
├── notebooks/
├── tests/
├── src/
└── assignments/
```

## Setup

### 1. Clone the repository

```powershell
git clone git@github.com:MendySte/AI-LLM-engineering-course.git
cd AI-LLM-engineering-course
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate it

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## Anthropic API

The hosted examples require an Anthropic API key.

Set it as an environment variable:

```powershell
$env:ANTHROPIC_API_KEY = "your-api-key"
```

Never commit API keys to Git.

## Local Model

The local example uses:

```text
Qwen/Qwen2.5-0.5B-Instruct
```

The model is automatically downloaded from Hugging Face on the first run and cached locally.

Run it with:

```powershell
python local_llm.py
```

## Key Learnings

The first stage of the project demonstrates several important differences between hosted and local LLMs.

A hosted model such as Claude provides strong output quality with minimal local compute requirements.

A small local model provides greater control and local inference, but output quality may be significantly lower.

For example, the local Qwen model successfully ran on the local machine but produced an incorrect explanation of a star schema. This provides a useful baseline for future grounding, evaluation, and RAG experiments.

See `reflections.md` for additional observations.

## Roadmap

The project will evolve throughout the course toward a grounded BI assistant using:

- Local open-source models
- Prompt engineering
- Evaluation
- Embeddings
- Vector search
- Retrieval-Augmented Generation (RAG)
- Qlik / BI / SQL knowledge sources
- Model comparison
- Additional AI engineering techniques introduced during the course

## Security

Sensitive information must never be committed to this repository.

The repository excludes local environments, secrets, model caches, and generated files where appropriate.