# 🧠 textprep

**textprep** is a lightweight Python library of preprocessing utilities for preparing raw text data for embedding, vectorization, and downstream NLP applications such as Retrieval-Augmented Generation (RAG), semantic search, and large language model (LLM) pipelines.

---

## Features

- Clean and normalize raw text
- Tokenize and split large text into chunks
- Strip metadata or stopwords (optional)
- Preprocess text from PDFs, HTML, markdown, etc.
- Easily pluggable into LLM pipelines (e.g., OpenAI, HuggingFace, LangChain)

---

## Installation

```bash
pip install textprep

git clone https://github.com/your-org/textprep.git
cd textprep
pip install -e .
```
## Usage
```
from textprep import clean_text, chunk_text

raw = """
This is a raw paragraph from a PDF or web page. It might have extra spaces, line breaks,
or inconsistent punctuation. Our goal is to clean it up and tokenize it.
"""

# Step 1: Clean the raw text
cleaned = clean_text(raw)

# Step 2: Chunk the text for embedding (e.g., 200 words per chunk)
chunks = chunk_text(cleaned, max_words=200)

for i, c in enumerate(chunks):
    print(f"Chunk {i+1}:\n{c}\n")
```
