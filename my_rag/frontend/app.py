import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖",
    layout="centered"
)


st.title("🤖 RAG Chatbot")
st.caption("Upload a document and ask questions from it")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False


with st.sidebar:
    st.header("📄 Upload Document")

    uploaded_file = st.file_uploader(
        "Upload PDF / TXT / DOCX",
        type=["pdf", "txt", "docx"]
    )

    if uploaded_file:
        if st.button("Upload Document"):
            with st.spinner("Indexing document... ⏳"):

                try:
                    response = requests.post(
                        f"{API_URL}/upload",
                        files={"file": (uploaded_file.name, uploaded_file.getvalue())}
                    )

                    if response.status_code == 200:
                        st.success("✅ Document uploaded and indexed successfully")
                        st.session_state.document_uploaded = True
                        st.session_state.messages = []
                    else:
                        st.error(response.text)

                except requests.exceptions.ConnectionError:
                    st.error("❌ Backend not running. Please start the server first.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.document_uploaded:

    user_input = st.chat_input("Ask a question about your document...")

    if user_input:
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking... 🤔"):

                try:
                    response = requests.post(
                        f"{API_URL}/ask",
                        json={"query": user_input}
                    )

                    if response.status_code == 200:
                        answer = response.json()["answer"]
                        st.markdown(answer)

                        st.session_state.messages.append(
                            {"role": "assistant", "content": answer}
                        )
                    else:
                        st.error(response.text)

                except requests.exceptions.ConnectionError:
                    st.error("❌ Backend not running.")

else:
    st.info("👈 Please upload a document first to start chatting.")