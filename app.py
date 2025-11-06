from flask import Flask,request,jsonify,render_template
from src.helper import download_embeddings 
from src.prompt import * 
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain 
from langchain_community.llms import Ollama  
from langchain.vectorstores import Chroma 
from langchain.memory import ConversationBufferMemory
from langchain.schema import AIMessage,HumanMessage

app=Flask(__name__)


# download embeddings to convert data into vector
embeddings=download_embeddings() 

# vector database directory
directory="vector_data"

# load vector data from vector database
vector_data=Chroma(
    persist_directory=directory,
    embedding_function=embeddings
)

#Create retriever
retriever=vector_data.as_retriever(search_type="similarity",search_kwargs={"k":3})

llm=Ollama(model="gemma3") 


#Add conversational memory
memory=ConversationBufferMemory(memory_key="chat_history",return_messages=True)

# Build chain with memory-aware prompt
question_answer_chain=create_stuff_documents_chain(llm=llm,prompt=prompt)
rag_chain=create_retrieval_chain(retriever,question_answer_chain)


@app.route("/")
def index(): 
    return render_template("index.html")


@app.route("/get",methods=["GET","POST"])
def chat(): 
    msg=request.form["msg"]
    print("USER INPUT:",msg)

    chat_hist_str="\n".join([
        f"user:{m.content}" if isinstance(m,HumanMessage) else f"bot:{m.content}"

        for m in memory.chat_memory.messages
    ])

    response=rag_chain.invoke({
        "input":msg,
        "chat_history":chat_hist_str
    })

    answer=response["answer"]

    print("RESPONSE:",answer)

    memory.chat_memory.add_message(HumanMessage(content=msg))
    memory.chat_memory.add_ai_message(AIMessage(content=answer))

    return str(answer)

@app.route("/reset")
def reset_memory(): 
    memory.clear()
    return "clear chat memory"


if __name__ == "__main__": 
    app.run(host="0.0.0.0",port=8080,debug=True)