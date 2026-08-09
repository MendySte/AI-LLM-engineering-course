# AI & LLM Engineering Course

A hands-on course project for learning how to build applications with large language models using Python.

This repository will evolve throughout the course and include hosted LLM integrations, prompt engineering, structured outputs, document-grounded question answering, and local open-source models.

## Current Status

The project currently includes a basic Python script that sends a chat completion request to OpenAI and prints the model's response.

## Project Structure

- `hello_llm.py` - Sends a simple prompt to a Claude model through Anthropic's OpenAI-compatible API.
- `requirements.txt` - Lists the Python dependencies.
- `.env.example` - Shows the required environment variables.
- `.gitignore` - Excludes local, generated, and sensitive files from Git.

## Requirements

- Python 3.12 or newer
- An Anthropic API key

## Setup

Clone the repository:

```bash
git clone https://github.com/MendySte/AI-LLM-engineering-course.git
cd AI-LLM-engineering-course
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

Set the OpenAI API key for the current PowerShell session:

```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-your-api-key"
```

Run the application:

```powershell
python hello_llm.py
```

## Planned Exercises

- System prompt experimentation
- Temperature comparison
- Structured JSON output
- Pydantic validation
- Document-grounded question answering
- Local open-source model execution

## Security

API keys, virtual environments, and local configuration files must never be committed to the repository.

Use `.env.example` only as a configuration template. Never add a real API key to this file.

