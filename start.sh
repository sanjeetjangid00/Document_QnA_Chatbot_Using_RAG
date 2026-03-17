#!/bin/bash

echo "Starting FastAPI Backend..."
cd /app/backend
python -m uvicorn fastapi_app:app --host 0.0.0.0 --port 8000 &

# Wait for the backend to initialize
sleep 3

echo "Starting Streamlit Frontend..."
cd /app/frontend
python -m streamlit run app.py --server.port 8501 --server.address 0.0.0.0
