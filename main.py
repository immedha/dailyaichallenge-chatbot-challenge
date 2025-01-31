"""
Streamlit is a python framework that allows you to maintain a simple UI for your application with no effort.
We will be using it to create a simple chatbot interface: displaying the previous messages and allowing the user to input a new message.

You need to learn just a couple of things first to use it: 
(1) what is session state: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state
(2) How to use the chat_message function for displaying the assistant/user messages in a chatbot interface: https://docs.streamlit.io/develop/api-reference/chat/st.chat_message
(3) How to get user input (text_input function): https://docs.streamlit.io/develop/api-reference/widgets/st.text_input

NOTE: To run your streamlit app, run the coommand `streamlit run main.py` in your terminal.
"""

import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Here we load the OpenAI API key from the environment variable and set it
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("API key not found. Please set the OPENAI_API_KEY in the .env file.")
else:
    openai.api_key = api_key

# TODO: Create an Open AI client object and set the API key

# TODO: Initialize an object to store the message history (in the session state)

# TODO: Here we will set up all the Streamlit display elements. 
# (1) Create a title for the streamlit page, 
# (2) display the previous message history using streamlit's chat_message function, and 
# (3) display an input element for the user's message

# TODO: Here we will handle the user submitting the message and getting the AI response.
# Remember that when calling the Open AI API, you need to include the entire message history in order for the AI to remember the conversation.

# TODO: Not only should you append the new AI response to the message history, but you also need to display the new respnse for now 
# because Streamlit will only display the updated message history on the NEXT render of the page.
