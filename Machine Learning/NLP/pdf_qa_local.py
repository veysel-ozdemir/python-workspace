import os

from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

MODEL = 'llama2'


def setup_qa_system(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load_and_split()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(model=MODEL)
    vector_store = FAISS.from_documents(chunks, embeddings)

    retriever = vector_store.as_retriever()
    llm = ChatOllama(
        model=MODEL,
        temperature=0,
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
    )

    return qa_chain


if __name__ == '__main__':
    qa_chain = setup_qa_system('papers/attention.pdf')

    while True:
        question = input('\nAsk a question (q to quit): ')
        if question.lower() == 'q':
            break

        answer = qa_chain.invoke(question)
        print('Answer:')
        print(answer['result'])
