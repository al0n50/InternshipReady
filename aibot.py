import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
import PyPDF2

# Make sure to run: pip install openai python-dotenv PyPDF2

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

st.title("AI Document Assistant")

# Initialize the OpenAI Client
if "client" not in st.session_state:
    st.session_state.client = OpenAI(api_key=api_key)

with st.sidebar:
    st.header("Setup")
    uploaded_file_ui = st.file_uploader(label="Upload your document", type=["pdf", "txt"])

    if uploaded_file_ui and "doc_text" not in st.session_state:
        with st.spinner("Extracting text from document..."):

            # Extract text based on file type
            if uploaded_file_ui.type == "application/pdf":
                reader = PyPDF2.PdfReader(uploaded_file_ui)
                text = "".join(page.extract_text() for page in reader.pages)
            else:
                text = uploaded_file_ui.getvalue().decode("utf-8")

            # Save the extracted text to the session state
            st.session_state.doc_text = text
            st.success("Document processed successfully!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask a question about the uploaded document:")
if prompt:
    if "doc_text" not in st.session_state:
        st.error("Please upload a document first!")
    else:
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Prepare the system instruction with the extracted document text
        system_instruction = f"You are a document expert. Answer questions ONLY using the following document text. If the answer isn't there, say you don't know.\n\nDocument Text:\n{st.session_state.doc_text}"

        # Build the message list for OpenAI
        api_messages = [{"role": "system", "content": system_instruction}] + st.session_state.messages

        # Call OpenAI Chat Completions API
        with st.chat_message("assistant"):
            response = st.session_state.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=api_messages
            )
            answer = response.choices[0].message.content
            st.markdown(answer)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": answer})