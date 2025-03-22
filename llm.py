import streamlit as st
import openai
import os

# Initialize the Sambanova API client
client = openai.OpenAI(
    api_key="6e22a00c-3212-4f27-b6ff-463251a47595",
    base_url="https://api.sambanova.ai/v1",
)

# Streamlit App Title
st.title("Chat with LLaMA 3 Model")

# Store the chat history in session state
if 'messages' not in st.session_state:
    st.session_state['messages'] = [{"role": "system", "content": "You are a helpful assistant."}]

# Function to call the Sambanova API
def generate_response(user_input):
    st.session_state['messages'].append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model='Meta-Llama-3.1-8B-Instruct',
        messages=st.session_state['messages'],
        temperature=0.1,
        top_p=0.1
    )
    
    # Accessing response using dot notation
    reply = response.choices[0].message.content
    st.session_state['messages'].append({"role": "assistant", "content": reply})
    return reply

# User input section
user_input = st.text_input("You: ", key="input")
if st.button("Send"):
    if user_input:
        reply = generate_response(user_input)
        st.write(f"Assistant: {reply}")

# Display the conversation history
if st.session_state['messages']:
    for message in st.session_state['messages']:
        role = message['role'].capitalize()
        content = message['content']
        st.write(f"{role}: {content}")
