from dotenv import load_dotenv
import os
import streamlit as st
from groq import Groq


# Load environment variables
load_dotenv()

# Get Groq API key
api_key = os.getenv("GROQ_API_KEY")

# Initialize client
client = Groq(api_key=api_key)

# Function to generate blog
def generate_blog(topic, style, length):
    prompt = f"Write a {length} blog post about '{topic}' in a {style} tone."
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", 
        messages=[
            {"role": "system", "content": "You are a creative AI blog writer."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Streamlit App
st.set_page_config(page_title=" Blog Generator")
st.header(" AI Blog Generator ")

topic = st.text_input("Enter blog topic:")
style = st.selectbox("Choose writing style:", ["Professional", "Casual", "Inspirational", "Technical"])
length = st.radio("Select blog length:", ["Short (200 words)", "Medium (400 words)", "Long (800+ words)"])

if st.button("Generate Blog"):
    if not topic.strip():
        st.warning("Please enter a topic!")
    else:
        with st.spinner("Generating your blog... "):
            blog = generate_blog(topic, style, length)
        st.subheader(" Generated Blog")
        st.write(blog)
