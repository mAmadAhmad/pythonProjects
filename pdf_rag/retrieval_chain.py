# retrieval_chain.py
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers.multi_query import MultiQueryRetriever


def setup_retrieval_chain(vector_db, model):
    llm = ChatOllama(model=model)

    query_prompt = PromptTemplate(
        input_variables=['question'],
        template="""You are an AI language model assistant. Your task is to generate five
        different versions of the given user question to retrieve relevant documents from
        a vector database. By generating multiple perspectives on the user question, your
        goal is to help the user overcome some of the limitations of the distance-based
        similarity search. Provide these alternative questions separated by newlines.
        Original question: {question}""",
    )

    retriever = MultiQueryRetriever.from_llm(
        vector_db.as_retriever(), llm, prompt=query_prompt
    )

    template = """Answer the question based ONLY on the following 
    context:{context}
    Question:{question}
    """

    prompt = ChatPromptTemplate.from_template(template)

    chain = ({'context': retriever, 'question': RunnablePassthrough()}
             | prompt
             | llm
             | StrOutputParser()
             )

    return chain
