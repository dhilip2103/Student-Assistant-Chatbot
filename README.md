# 📘 Student Assistant Chatbot

A **Django-based chatbot** for students 📚.  
Upload your **PDF/DOCX notes** and ask questions.  
The chatbot uses **Groq LLaMA-3** for reasoning and **HuggingFace embeddings** with **ChromaDB** for semantic search.

---

## 🚀 Features
- 📂 Upload notes (PDF / DOCX)
- 🔍 Extract and process text
- 🧠 Create vector embeddings using HuggingFace
- 🗄️ Store data in ChromaDB
- 🤖 Ask questions and get answers with Groq LLaMA-3
- 💾 Chat history maintained in session
- 🎨 Simple Bootstrap frontend

---

## 🛠️ Tech Stack
- **Backend:** Django, LangChain
- **LLM:** Groq (LLaMA-3-8B)
- **Embeddings:** HuggingFace (`sentence-transformers/all-MiniLM-L6-v2`)
- **Vector Store:** ChromaDB
- **Frontend:** HTML, CSS, Bootstrap

---

## ⚡ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/student-assistant-chatbot.git
cd student-assistant-chatbot
