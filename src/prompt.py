from langchain.prompts import ChatPromptTemplate

# Define the system prompt that sets the behavior and tone of the AI assistant
system_prompt=(
    "you are travel question answer ai assistant "
    "you are polite and friendly "
    "answer should be in three sentences maximum and concise"
    "\n\n"
    "{context}"
)

# Create a chat prompt template that structures the conversation
prompt=ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt),
        ("human","{input}")
    ]
)