from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2'
)

# Create collection once
vector_db = Chroma(
    collection_name='rag_collection',
    embedding_function=embedding_model,
    persist_directory="./Chroma_db"
)

def add_documents(documents):
    vector_db.add_documents(documents)


def get_retriever():
    return vector_db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )


def reset_collection():
    all_docs = vector_db._collection.get()
    ids = all_docs.get("ids")

    if ids:
        vector_db._collection.delete(ids=ids)