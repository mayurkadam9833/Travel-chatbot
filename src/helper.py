from langchain.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings



# Function to load files [pdf] from path and extract data into document
def load_pdf_file(data): 
    loader=DirectoryLoader(
        data, 
        glob="*.pdf", 
        loader_cls=PyPDFLoader
    )
    documents=loader.load()
    return documents 

# Function take extracted data and create text chunk
def text_splitter(data): 
    text_split=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=20)
    text_chunk=text_split.split_documents(data)
    return text_chunk


# Function download embeddings from Huggingface 
def download_embeddings(): 
    embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings