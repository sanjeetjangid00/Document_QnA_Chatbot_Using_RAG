# 🤖 RAG Chatbot

This project is a Retrieval-Augmented Generation (RAG) application that allows users to upload documents (PDF, TXT, DOCX) and ask questions based on their content. It consists of a **FastAPI** backend for handling file processing, embeddings, and querying, and a **Streamlit** frontend for an interactive chatbot interface.

## 🚀 Features

- **Document Upload**: Supports `.pdf`, `.txt`, and `.docx` file formats.
- **Text Processing**: Automatically loads, cleans extra spaces, and splits documents into manageable chunks.
- **Vector Storage**: Uses **ChromaDB** with HuggingFace embeddings (`sentence-transformers/all-MiniLM-L6-v2`).
- **Conversational AI**: Uses Groq (`ChatGroq` with `openai/gpt-oss-20b` model) to answer questions based on the uploaded document context.
- **Clean Architecture**: Decoupled backend (FastAPI) and frontend (Streamlit).

## 📂 Project Structure

```text
my_rag/
├── backend/
│   ├── document_load.py   # Document loading logic (PDF, TXT, DOCX)
│   ├── fastapi_app.py     # FastAPI application and endpoints
│   ├── rag_app.py         # RAG LLM setup and query chain
│   ├── requirements.txt   # Backend dependencies
│   ├── splitter.py        # Text splitting configuration
│   └── vector_db.py       # ChromaDB setup and embedding logic
├── frontend/
│   └── app.py             # Streamlit web interface
├── myenv/                 # Python virtual environment
└── run.bat                # Batch script to start both backend and frontend servers
```

## 🛠️ Prerequisites

- Python 3.8+
- [Groq API Key](https://console.groq.com/keys) (Add it to `backend/.env` file as `GROQ_API_KEY`)

## ⚙️ Setup and Installation

1. Create a `.env` file inside the `backend` folder and add your environment variables (e.g., `GROQ_API_KEY=your_key_here`).
2. Make sure the dependencies are installed via `pip install -r backend/requirements.txt` and `pip install streamlit requests`. 
   *(Note: The provided `run.bat` uses the virtual environment `myenv` which should have these installed).*

## ▶️ Running the Application

You can easily run both servers using the provided script:
- **Windows**: Double-click `run.bat` or run it from the terminal:
  ```powershell
  .\run.bat
  ```

This will start the FastAPI backend on port 8000 and the Streamlit frontend in your default browser.

### 🐳 Using Docker

You can also run the entire application using Docker:

1. Build the Docker image:
   ```bash
   docker build -t rag-app .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 -p 8501:8501 rag-app
   ```

The Streamlit frontend will be available at `http://localhost:8501` and the FastAPI backend at `http://localhost:8000`.
