# AI Blog Generator with Groq
This is a simple web application built with Streamlit and the Groq API to quickly generate blog posts on any topic with customizable style and length. It uses the Llama-3.1-8b-Instant model for fast, high-quality content generation.
 
---

## Features
* **Ultra-Fast Generation:** Leverages the high-speed inference of the Groq API (using `Llama-3.1-8b-Instant`).
* **Topic Input:** Define the subject for the blog post.
* **Style Selection:** Choose from **Professional**, **Casual**, **Inspirational**, or **Technical** tones.
* **Length Control:** Select **Short** (200 words), **Medium** (400 words), or **Long** (600+ words).

---

## 🧩 Tech Stack
- **Python**
- **Streamlit**
- **Groq API (LLaMA 3 model)**
- **dotenv** (for API key management)

---

## Project Structure
AI-Blog-Generator/
│
├── blog_app.py          # Main Streamlit app
├── requirements.txt     # Python dependencies
├── .env                 # Contains your Groq API key
└── README.md            # Project documentation
