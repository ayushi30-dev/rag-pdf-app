# Local PDF RAG Application (Python + LangChain + Ollama + ChromaDB)

A 100% local Retrieval-Augmented Generation (RAG) application that answers questions grounded strictly in a PDF document (`data/company_handbook.pdf`) using **Ollama** and **ChromaDB**—no paid API keys required.

## Project Structure

rag-pdf-app/
├── data/
│   └── company_handbook.pdf   # Sample PDF knowledge base
├── create_sample_pdf.py       # Generates the sample PDF locally
├── ingest.py                  # Loads PDF, chunks text, and saves embeddings to ChromaDB
├── ask.py                     # Retrieves relevant chunks and generates grounded answers
├── .gitignore
└── README.md


## Prerequisites

1. **Python 3.10+** — Download from [python.org](https://www.python.org/) (check **"Add Python to PATH"** during installation on Windows).
2. **Ollama** — Download and install from [ollama.com](https://ollama.com/), and ensure the Ollama service is running.

## Setup & Run Instructions

### 1. Clone or Pull the Repository

git clone [https://github.com/ayushi30-dev/rag-pdf-app.git](https://github.com/ayushi30-dev/rag-pdf-app.git)
cd rag-pdf-app


If you already cloned the repository locally:

git pull origin main

### 2. Create and Activate a Virtual Environment
python -m venv .venv


Activate the environment based on your terminal in VSCode:

* **Windows (PowerShell):**
  .\.venv\Scripts\Activate.ps1
  
* **Windows (Command Prompt / `cmd.exe`):**
  .\.venv\Scripts\activate.bat
  
* **Windows (Git Bash):**
  source .venv/Scripts/activate
  
* **macOS / Linux:**
  
  source .venv/bin/activate

Confirm `(.venv)` appears at the beginning of your terminal prompt before proceeding.

### 3. Install Python Dependencies

python -m pip install langchain langchain-community langchain-ollama langchain-chroma chromadb pypdf fpdf2


### 4. Pull Required Ollama Models

Download the embedding model and local chat model:

ollama pull nomic-embed-text
ollama pull qwen2.5:3b

Verify both models are available locally:

ollama list


> **Windows Troubleshooting (`ollama pull` timeout):** If `ollama pull` times out while connecting to an IPv6 address (`[2606:4700:...]`), open **Network Connections** (`ncpa.cpl`), open **Properties** on your active Wi-Fi/Ethernet adapter, uncheck **Internet Protocol Version 6 (TCP/IPv6)**, and re-run `ollama pull`.

### 5. (Optional) Generate the Sample PDF

If data/company_handbook.pdf is missing or you want to recreate it:

mkdir -p data
python create_sample_pdf.py


### 6. Ingest the PDF into ChromaDB

Chunk the PDF and generate local vector embeddings in `./chroma_db` (run this once before querying, and re-run whenever `data/company_handbook.pdf` changes):

python ingest.py

### 7. Ask Questions Against the PDF

python ask.py

#### Sample Test Queries
* **In-scope query:** `What is the annual learning allowance and how many earned leaves do employees get?`
* **Out-of-scope query (hallucination check):** `What is the parental leave policy?`# rag-pdf-app
