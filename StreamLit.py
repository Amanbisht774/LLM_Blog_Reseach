import os 
import warnings
warnings.filterwarnings("ignore")
import langchain
from langchain_community.llms import OpenAI
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
import streamlit as st
import pickle
import time
os.environ["OPENAI_API_KEY"]=""
st.title("URL Blog Analysis")
st.sidebar.title("INPUT URL you want to analize")

urls=[]

for i in range(3):
    url=st.sidebar.text_input(f"URL{i+1}")
    urls.append(url)

url_clicked=st.sidebar.button("Analize")
file_path="FAISS"
main_place=st.empty()
llms=OpenAI(temperature=0.7,max_tokens=500)
if url_clicked:
    
    loader=UnstructuredURLLoader(urls=urls)
    main_place.text("Start Collecting data from URLS....")
    data=loader.load()

    text_splitter= RecursiveCharacterTextSplitter(separators=["\n\n","\n",".",","], chunk_size=1000)
    main_place.text("Splitting the data into chunks...")

    docs=text_splitter.split_documents(data)

    embedding=OpenAIEmbeddings()

    vector_db=FAISS.from_documents(docs,embedding)
    main_place.text("Creating FAISS DB for data....")

    vector_db.save_local(file_path)
    main_place.text("Data is saved and ready for RAG")

query=main_place.text_input("Question:")
embedding=OpenAIEmbeddings()
if query:

    vector_db=FAISS.load_local(file_path,embeddings=embedding,allow_dangerous_deserialization=True)
    chain=RetrievalQAWithSourcesChain.from_llm(llms,retriever=vector_db.as_retriever())
    result=chain({"question":query},return_only_outputs=True)
    st.header("Answer")
    st.write(result["answer"])

    sources=result.get("sources","")
    if sources:
        st.subheader("Source:")
        source_list=sources.split("\n")
        for source in source_list:
            st.write(source)

    
