import os 
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

load_dotenv()

#init embedding model
embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# init pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("shop-product-catalog")

# init vectorstore
VectorStore = PineconeVectorStore(
    index = index,
    embedding = embedding_model,
    text_key="ProductDescription"
)

