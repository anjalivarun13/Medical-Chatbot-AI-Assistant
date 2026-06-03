import streamlit as st
import os
import datetime
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from src.helper import download_hugging_face_embeddings
from src.prompt import system_prompt

# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Page setup
st.set_page_config(page_title="Medical Chatbot", page_icon="🩺")
st.title("🩺 Medical Chatbot")
st.write("Ask me anything!")

# Sidebar with clear history button
with st.sidebar:
    st.header("⚙️ Settings")
    if st.button("Clear chat history"):
        st.session_state.messages = []
        st.rerun()

# Custom CSS for chat bubbles
st.markdown(
    """
    <style>
    .stChatMessage[data-testid="stChatMessage-user"] {
        background-color: #d4f8d4; /* light green */
        border-radius: 12px;
        padding: 10px;
    }
    .stChatMessage[data-testid="stChatMessage-assistant"] {
        background-color: #dce8ff; /* light blue */
        border-radius: 12px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar=msg["avatar"]):
        st.markdown(f"**{msg['time']}**  \n{msg['content']}")

# Input box at the bottom
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "avatar": "🟢",
        "time": datetime.datetime.now().strftime("%H:%M"),
        "content": user_input
    })

    # Embeddings + retriever
    embeddings = download_hugging_face_embeddings()
    docsearch = PineconeVectorStore.from_existing_index(
        index_name="medical-chatbot",
        embedding=embeddings
    )
    retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    # Google Generative AI model
    chatmodel = ChatGoogleGenerativeAI(
        model="models/gemini-flash-latest",
        google_api_key=GOOGLE_API_KEY
    )

    # Prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    # Build RAG chain
    question_answer_chain = create_stuff_documents_chain(chatmodel, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    # Get response
    response = rag_chain.invoke({"input": user_input})
    bot_answer = response["answer"]

    # Add bot message
    st.session_state.messages.append({
        "role": "assistant",
        "avatar": "👨‍⚕️",
        "time": datetime.datetime.now().strftime("%H:%M"),
        "content": bot_answer
    })

    st.rerun()
