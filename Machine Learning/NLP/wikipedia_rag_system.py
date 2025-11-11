import os
from dotenv import load_dotenv
import streamlit as st
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.readers.wikipedia import WikipediaReader
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage

load_dotenv()
INDEX_DIR = 'wiki_rag'
PAGES = [
    "World War II",
    "Korean War",
    "Vietnam War",
    "Suez Crisis",
    "Falklands War",
    "Gulf War",
    "Kosovo War",
    "War in Afghanistan",
    "Iraq War",
    "Syrian Civil War",
    "Yemeni civil war (2014–present)",
    "Libyan Civil War",
    "Russo-Ukrainian War",
    "Second Nagorno-Karabakh War",
    "Second Lebanon War",
    "Somali Civil War",
    "South Sudanese Civil War",
    "Central African Republic Civil War",
    "Tigray War",
]
MODEL = "<YOUR_MODEL>"
EMBEDDING_MODEL = "<YOUR_EMBEDDING_MODEL>"


@st.cache_resource
def get_index():
    if os.path.isdir(INDEX_DIR):
        storage = StorageContext.from_defaults(persist_dir=INDEX_DIR)
        return load_index_from_storage(storage)

    docs = WikipediaReader().load_data(pages=PAGES, auto_suggest=False)
    embedding_model = OpenAIEmbedding(
        api_key=os.getenv("OPENAI_API_KEY"),
        model=EMBEDDING_MODEL
    )
    index = VectorStoreIndex.from_documents(documents=docs, embedding_model=embedding_model)
    index.storage_context.persist(persist_dir=INDEX_DIR)

    return index


@st.cache_resource
def get_query_engine():
    index = get_index()

    llm = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        model=MODEL,
        temperature=0
    )

    return index.as_query_engine(llm=llm, similarity_top_k=3)


def main():
    st.title("Wikipedia RAG System")

    question = st.text_input('Ask a question')

    if st.button("Submit") and question:
        with st.spinner('Thinking...'):
            qa = get_query_engine()
            response = qa.query(question)

        st.subheader('Answer')
        st.write(response.response)

        st.subheader('Retrieved context')

        for src in response.source_nodes:
            st.markdown(src.node.get_content())


if __name__ == '__main__':
    main()
