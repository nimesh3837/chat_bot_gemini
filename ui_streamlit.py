import streamlit as st
from client_api_service import ClientApiService

st.title("Zomato Customer Service")

client_api_service = ClientApiService()

# Initialize UI history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello, how can I help you?"
        }
    ]

# Display old messages
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# New user message
user_message = st.chat_input("Your question")

if user_message:

    # Add user message to UI history
    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    # Get response from your API
    response = client_api_service.chat_bot(user_message).message
    
    # Add assistant response to UI history
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    # Rerun to display the updated history
    st.rerun()