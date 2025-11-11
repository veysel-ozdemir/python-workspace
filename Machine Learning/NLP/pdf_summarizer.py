import os
from dotenv import load_dotenv
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI

load_dotenv()
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
GEMMA_MODEL = "google/gemma-3n-e2b-it:free"
LLAMA_MODEL = "meta-llama/llama-3.3-8b-instruct:free"


def summarize_pdf(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load_and_split()
    llm = ChatOpenAI(
        base_url=OPENROUTER_BASE_URL,
        api_key=OPENROUTER_API_KEY,
        model_name=GEMMA_MODEL
    )
    chain = load_summarize_chain(llm, chain_type='map_reduce')
    summary = chain.invoke(docs)

    return summary


if __name__ == '__main__':
    summary = summarize_pdf('papers/bitcoin.pdf')

    print('Summary:')
    print(summary['output_text'])
