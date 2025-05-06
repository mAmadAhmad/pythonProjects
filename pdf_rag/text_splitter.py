# text_splitter.py
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(data):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=300)
    chunks = splitter.split_documents(data)
    print('done splitting....')
    return chunks
