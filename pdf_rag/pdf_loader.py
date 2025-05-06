# pdf_loader.py
from langchain_community.document_loaders import UnstructuredPDFLoader


def load_pdf(doc_path):
    try:
        if doc_path:
            loader = UnstructuredPDFLoader(file_path=doc_path)
            data = loader.load()
            print('done loading pdf....')
            return data
        else:
            print('no pdf found....')
            return None
    except Exception as e:
        print(f'An error occurred while loading the pdf: {e}')
        return None
