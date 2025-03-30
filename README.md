# URL Blog Analysis

## 📝 Overview

This is a Streamlit-based web application that allows users to analyze the content of multiple blog URLs and extract insights using Retrieval-Augmented Generation (RAG) with OpenAI's language model. The application loads data from the given URLs, processes it into a vector database using FAISS, and enables users to query the stored information interactively.

## 🚀 Features

🔗 URL-Based Data Extraction: Users can input up to three URLs, from which the application scrapes text data.

📄 Text Processing & Chunking: Uses RecursiveCharacterTextSplitter to split extracted text into manageable chunks.

🗃️ Vector Database Creation: Stores embeddings using FAISS for efficient retrieval.

🔍 Retrieval-Augmented Generation (RAG): Enables users to query the stored knowledge and receive answers with sources.

🤖 OpenAI Language Model: Utilizes OpenAI's LLM with a temperature setting of 0.7 for response generation.

## 🛠️ Tech Stack

🐍 Python

🎨 Streamlit

🏗 LangChain

📚 FAISS

🧠 OpenAI API

🌐 Unstructured URL Loader

🤗 Hugging Face Embeddings (Optional)

## 📥 Installation

Clone the repository:

git clone https://github.com/yourusername/url-blog-analysis.git
cd url-blog-analysis

Install dependencies:

pip install -r requirements.txt

Set up your OpenAI API key:

export OPENAI_API_KEY="your-api-key"

Run the Streamlit application:

streamlit run app.py

## 🎯 Usage

Enter up to three blog URLs in the sidebar.

Click "Analyze" to start processing the content.

Once processing is complete, enter a question in the input field.

View the generated answer along with source references.

## 🔎 Notes

📌 The application saves the FAISS database locally for efficient retrieval.

⚠️ Ensure you have a valid OpenAI API key before running the app.
