---
description: Start the RAG Chatbot FastAPI backend and Streamlit frontend
---

# Execution Workflow for RAG Chatbot

This workflow will start the FastAPI backend server and the Streamlit frontend server for the RAG chatbot application.

**Note**: The backend automatically cleans extra spaces from uploaded documents during the embedding stage.

1. First, ensure your `.env` file is set up in `backend/.env` with your API keys (e.g., `GROQ_API_KEY`).
2. Run the `run.bat` script which will start both the FastAPI backend and Streamlit frontend.

// turbo
```powershell
.\run.bat
```

3. The script opens two separate CMD windows and starts both servers. You can interact with the app in your web browser.

---
### Alternative: Run with Docker

1. Build the Docker image:
// turbo
```powershell
docker build -t rag-app .
```

2. Run the container:
// turbo
```powershell
docker run -p 8000:8000 -p 8501:8501 rag-app
```
