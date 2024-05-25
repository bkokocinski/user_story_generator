import streamlit as st
from groq import Groq
import os

st.title("🗂️ User story generator")

client = Groq(
    api_key = os.environ['GROQ_API_KEY']
)

if prompt := st.chat_input():
    st.chat_message("user").write(prompt)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"write a short user centric user story based on the given prompt: {prompt}, never add any introduction like Here is a user-centric user story based on the prompt, follow the example - "
                           f"As a potato lover, I want to be able to mash potatoes so that they are easy to cook and have a smooth texture.",
            }
        ],
        model="llama3-8b-8192",
    )
    st.chat_message("assistant").write(chat_completion.choices[0].message.content)
