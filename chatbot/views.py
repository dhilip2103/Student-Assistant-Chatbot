from django.shortcuts import render
import os
from django.shortcuts import render, redirect
from django.conf import settings
from .utils import extract_text
from .vector_store import build_vector_store_from_text, load_vector_store
from .chatbot_engine import get_qa_chain

PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIRECTORY", "chromadb_data")

def chatbot_view(request):
    answer = ""
    sources = []
    # use session to store chat history
    chat_history = request.session.get('chat_history', [])

    if request.method == "POST":
        # File upload
        if 'file' in request.FILES:
            f = request.FILES['file']
            save_path = os.path.join(settings.MEDIA_ROOT, f.name)
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
            with open(save_path, 'wb+') as dest:
                for chunk in f.chunks():
                    dest.write(chunk)
            text = extract_text(save_path)
            if text.strip():
                build_vector_store_from_text(text, persist_directory=PERSIST_DIR)
                answer = "✅ File uploaded and processed. You can ask questions now."
            else:
                answer = "⚠️ Could not extract text from file."

        # Question ask
        elif 'question' in request.POST:
            question = request.POST.get('question', '').strip()
            if not question:
                answer = "Please enter a question."
            else:
                # load vectorstore and query
                try:
                    vectordb = load_vector_store(PERSIST_DIR)
                    qa = get_qa_chain(vectordb)
                    response = qa({"question": question, "chat_history": chat_history})
                    answer = response.get("answer", "No answer returned.")
                    # collect source docs (optional)
                    docs = response.get("source_documents", [])
                    sources = [getattr(d, "metadata", {}) for d in docs]
                    # update session chat history
                    chat_history.append((question, answer))
                    request.session['chat_history'] = chat_history[-20:]  # keep last 20
                except Exception as e:
                    answer = f"Error while querying vector store: {e}"

    return render(request, "chatbot/chatbot.html", {"answer": answer, "sources": sources, "chat_history": chat_history})
