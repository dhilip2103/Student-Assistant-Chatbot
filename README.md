# Student Assistant Chatbot

Student Assistant Chatbot

A web-based chatbot that helps students extract information from PDF and Word documents and answer questions using AI.


Features
---------------------------------------------------------------
Upload PDF and DOCX files to extract text

Ask questions based on the uploaded documents

AI-powered answers using Groq API (LLM)

Safe environment variables for API keys


Tech Stack
-------------------------------------------------------------------
Backend: Python, Groq API

Frontend: HTML, CSS, JavaScript

Libraries: PyPDF2, python-docx, dotenv

Environment Management: .env for secret API keys

Version Control: Git, GitHub



Installation :

Clone the repo:
---------------------------------------------------------------------
git clone https://github.com/dhilip2103/Student-Assistant-Chatbot.git


Install dependencies:
-------------------------------
pip install -r requirements.txt


Create a .env file in project root and add your Groq API key:
-------------------------------------------------------------
GROQ_API_KEY=your_api_key_here


Run the application:
--------------------
python app.py

Usage
------------------------------------------------------
Upload a PDF or DOCX file
Ask your question in the input field
The AI chatbot responds based on the uploaded document

Note
---------------------------
Keep your .env file private

Do not commit secrets to GitHub
