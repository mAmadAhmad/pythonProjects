# main.py
from pdf_loader import load_pdf
from text_splitter import split_text
from vector_db import create_vector_db
from retrieval_chain import setup_retrieval_chain

# Step 1: Load the PDF
doc_path = "Placement DSA Questions2.pdf"
data = load_pdf(doc_path)

if data:
    # Step 2: Split the text
    chunks = split_text(data)

    # Step 3: Create the vector database
    vector_db = create_vector_db(chunks)

    if vector_db:
        # Step 4: Set up the retrieval chain
        model = "deepseek-r1:1.5b"
        chain = setup_retrieval_chain(vector_db, model)

        # Step 5: Ask questions
        while True:
            question = input("Ask a question (or type 'exit' to quit): ")
            if question.lower() == 'exit':
                break
            res = chain.invoke(input=(question,))
            print(res)