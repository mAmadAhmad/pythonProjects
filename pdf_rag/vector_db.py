# vector_db.py
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
import ollama


def create_vector_db(chunks):
    try:
        ollama.pull('nomic-embed-text')
        vector_db = Chroma.from_documents(
            documents=chunks,
            embedding=OllamaEmbeddings(model='nomic-embed-text'),
            collection_name='simple_rag',
        )
        print('Done adding to vector database....')
        return vector_db
    except Exception as e:
        print(e)
        return None
