from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from document_load import document_loader
from splitter import text_splitter
from vector_db import add_documents, reset_collection
from rag_app import ask_llm
import os
import shutil
import re

app = FastAPI(title="RAG API")

UPLOAD_DIR = "uploaded_files"

class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    answer: str


class UploadResponse(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "RAG API is running"}


@app.post("/upload", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    try:
        # 1 Clear old embeddings
        reset_collection()

        # 2 Delete old uploaded files
        if os.path.exists(UPLOAD_DIR):
            shutil.rmtree(UPLOAD_DIR)

        os.makedirs(UPLOAD_DIR, exist_ok=True)

        # 3 Save new file
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        # 4 Load document
        documents = document_loader(file_path)

        # Add metadata and clean extra spaces from content
        for doc in documents:
            doc.metadata["source"] = file.filename
            doc.page_content = re.sub(r'\s+', ' ', doc.page_content).strip()

        # 5 Split
        splitted_docs = text_splitter(documents)

        # 6 Store embeddings
        add_documents(splitted_docs)

        return UploadResponse(
            message="Old data deleted. New file indexed successfully."
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ==============================
# Ask Endpoint
# ==============================

@app.post("/ask", response_model=QueryResponse)
def ask_query(request: QueryRequest):
    try:
        answer = ask_llm(request.query)
        return QueryResponse(answer=answer)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))