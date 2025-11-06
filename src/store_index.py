from langchain.vectorstores import Chroma  
from src.helper import load_pdf_file,text_splitter,download_embeddings 

# extract data from pdf files
extracted_data=load_pdf_file("Data/")

# split data into text chunk 
text_chunk=text_splitter(extracted_data)

# download embeddings to convert data into vector
embeddings=download_embeddings() 

# vector database directory
directory="vector_data"

# creating vector data at defined path by using huggingface embedding model
vector_database=Chroma.from_documents(
    documents=text_chunk,
    persist_directory=directory, 
    embedding=embeddings
)