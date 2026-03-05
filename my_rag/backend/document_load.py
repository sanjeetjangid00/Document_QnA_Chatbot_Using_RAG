from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader


def document_loader(file_path:str):
    if file_path.lower().endswith('.pdf'):
        file = PyPDFLoader(file_path)

    elif file_path.lower().endswith('.txt'):
        file = TextLoader(file_path, encoding="utf-8")

    elif file_path.lower().endswith('.docx'):
        file = Docx2txtLoader(file_path)

    else:
        raise ValueError("Unsupported file format")
    document = file.load()
    return document