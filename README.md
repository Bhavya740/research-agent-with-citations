# research-agent-with-citations
AI Research Agent with Citations using Python and Groq API

# Research Agent with Citations

## Overview

This project is a simple AI Research Agent built using Python and the Groq API.

The agent answers research questions using only the provided source documents and includes citations for every answer.

---

## Features

- Accepts user questions
- Uses Groq Llama 3.3 70B model
- Answers only from provided sources
- Includes source citations
- Prevents unsupported answers

---

## Technologies Used

- Python
- Groq API
- Llama 3.3 70B Versatile

---

## Project Structure

```
research-agent-with-citations/
│
├── app.py
├── requirements.txt
├── sample_questions.txt
└── README.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python app.py
```

Enter your Groq API Key when prompted.

Then ask questions such as:

- What is RAG?
- What is Machine Learning?
- What is Generative AI?

---

## Sample Output

Question:

```
What is RAG?
```

Answer:

```
Retrieval-Augmented Generation (RAG) retrieves relevant documents before generating an answer.
It reduces hallucinations and provides answers with citations.

Source: Source 3
```

---

## Trade-offs

- Uses embedded text sources instead of external document retrieval.
- Uses prompt-based citation instead of vector databases.
- Designed to be simple, easy to understand, and easy to run.

---

## Future Improvements

- PDF support
- Web search
- Vector database
- Semantic search
- Multiple document support
