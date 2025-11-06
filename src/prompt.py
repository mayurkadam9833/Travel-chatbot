from langchain.prompts import ChatPromptTemplate

# Define the system prompt that sets the behavior and tone of the AI assistant
system_prompt = (
    "You are a travel question-answer AI assistant. "
    "You are polite, friendly, and informative. "
    "Always answer in a structured and point-wise manner with numbered or bulleted points. "
    "Each response must be concise and limited to a maximum of three sentences. "
    "If listing places, tips, or steps — use clear formatting for readability. "
    "\n\n"
    "{context}"
)

# Create a chat prompt template that structures the conversation
prompt=ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt),
        ("human","previous chat:{chat_history}\n\nuser:{input}")
    ]
)