# RAG System

A minimal Retrieval-Augmented Generation (RAG) system.

## Project Structure

```
RAG/
├── src/                    # Source code
│   ├── rag/               # Main RAG package
│   │   ├── retriever/     # Document retrieval
│   │   ├── generator/     # Response generation
│   │   └── utils/         # Utility functions
├── data/                   # Data storage
│   ├── documents/         # Source documents
│   └── vectorstore/       # Vector database
├── config/                 # Configuration files
├── tests/                  # Test files
└── main.py                # Entry point
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

