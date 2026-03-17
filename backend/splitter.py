from langchain_text_splitters import RecursiveCharacterTextSplitter

def text_splitter(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 2000, chunk_overlap = 200)
    docs = text_splitter.split_documents(documents)
    return docs
