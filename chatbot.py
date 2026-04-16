import os
from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Load API key
load_dotenv()

# Step 1: Create vector database
def create_vector_store():
    loader = TextLoader("data/db_notes.txt")
    documents = loader.load()

    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    docs = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)

    db.save_local("embeddings")

# Step 2: Load chatbot
def load_chatbot():
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local("embeddings", embeddings)

    retriever = db.as_retriever()

    llm = ChatOpenAI(model_name="gpt-3.5-turbo")

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    return qa
