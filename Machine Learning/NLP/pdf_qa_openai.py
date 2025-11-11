import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.chains import PebbloRetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
MODEL_NAME = '<YOUR_MODEL_NAME>'


def setup_qa_system(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load_and_split()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings(
        api_key=os.getenv("OPENAI_API_KEY"),
    )
    vector_store = FAISS.from_documents(chunks, embeddings)

    retriever = vector_store.as_retriever()
    llm = ChatOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        model_name=MODEL_NAME,
        temperature=0,
    )

    qa_chain = PebbloRetrievalQA.from_chain_type(llm, retriever)

    return qa_chain


if __name__ == '__main__':
    qa_chain = setup_qa_system('papers/bitcoin.pdf')

    while True:
        question = input('\nAsk a question: ')
        if question.lower() == 'q':
            break

        answer = qa_chain.invoke(question)
        print('Answer: {}'.format(answer))
