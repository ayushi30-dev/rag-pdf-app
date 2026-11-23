from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

PDF_PATH = "data/company_handbook.pdf"
PERSIST_DIR = "./chroma_db"
EMBED_MODEL = "nomic-embed-text"

def main():
    # 1. Load PDF pages
    loader = PyPDFLoader(PDF_PATH)
    pages = loader.load()
    print(f"Loaded {len(pages)} page(s) from {PDF_PATH}")

    # 2. Split into overlapping chunks so sentences aren't cut off mid-thought
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=120
    )
    chunks = splitter.split_documents(pages)
    print(f"Split into {len(chunks)} chunk(s)")

    # 3. Embed chunks and store persistently in ChromaDB
    embeddings = OllamaEmbeddings(model=EMBED_MODEL)
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=PERSIST_DIR
    )
    print(f"Saved embeddings to {PERSIST_DIR}")

if __name__ == "__main__":
    main()