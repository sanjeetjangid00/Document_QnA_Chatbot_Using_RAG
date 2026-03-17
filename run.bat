@echo off

echo Starting Backend...
start cmd /k "cd backend && ..\myenv\Scripts\python -m uvicorn fastapi_app:app --host 127.0.0.1 --port 8000"

timeout /t 3

echo Starting Frontend...
start cmd /k "cd frontend && ..\myenv\Scripts\python -m streamlit run app.py"

echo Both servers started successfully.