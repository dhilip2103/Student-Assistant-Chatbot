from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def build_vector_store_from_text(text, persist_directory=None):
    if persist_directory is None:
        persist_directory = os.getenv("CHROMA_PERSIST_DIRECTORY", "chromadb_data")

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma.from_texts(texts, embeddings, persist_directory=persist_directory)
    return vectordb

def load_vector_store(persist_directory=None):
    if persist_directory is None:
        persist_directory = os.getenv("CHROMA_PERSIST_DIRECTORY", "chromadb_data")

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    return vectordb
