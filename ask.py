from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

PERSIST_DIR = "./chroma_db"
EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL = "qwen2.5:3b"

PROMPT = ChatPromptTemplate.from_template(
    """Answer the user's question using ONLY the context below.
If the answer is not in the context, say "I don't know based on the provided PDF."

Context:
{context}

Question:
{question}
"""
)

def format_docs(docs):
    return "\n\n---\n\n".join(doc.page_content for doc in docs)

def main():
    embeddings = OllamaEmbeddings(model=EMBED_MODEL)
    vectorstore = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embeddings
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    llm = ChatOllama(model=CHAT_MODEL, temperature=0)

    question = input("Ask a question about the handbook: ").strip()
    retrieved_docs = retriever.invoke(question)
    context_text = format_docs(retrieved_docs)

    chain = PROMPT | llm | StrOutputParser()
    answer = chain.invoke({"context": context_text, "question": question})

    print("\nAnswer:\n" + answer)

if __name__ == "__main__":
    main()