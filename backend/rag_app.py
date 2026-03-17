from langchain_groq import ChatGroq
from vector_db import get_retriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model = 'openai/gpt-oss-20b')

parser = StrOutputParser()

def chat_template():
    prompt = ChatPromptTemplate.from_template(
        """
        Use the provided context to answer the question. If the answer is not contained
        in the context, say "I don't know".

        Context:
        {context}

        Question:
        {question}
        """
    )

    return prompt

def qa_chain(prompt, retriever):
    rag_chain=(
        {
            "context": retriever,
            "question" : RunnablePassthrough()
        }
        |
        prompt | llm
    )

    return rag_chain
chain = qa_chain(chat_template(), get_retriever())

def ask_llm(question:str):
    response = chain.invoke(question)
    return parser.invoke(response)

