# agent/rag.py

import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

def get_topic_benchmark_context():
    """
    Load the topic_mastery.pdf and return the combined text content.
    This simulates retrieval-augmented generation (RAG) by embedding
    the raw text into the prompt.
    """
    loader = PyPDFLoader("docs/topic_mastery.pdf")
    pages = loader.load()
    full_text = "\n".join([doc.page_content for doc in pages])
    return full_text
