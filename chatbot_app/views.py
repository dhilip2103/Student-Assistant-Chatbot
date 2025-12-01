from django.shortcuts import render
from django.http import JsonResponse
from .utils import extract_text_from_pdf, extract_text_from_docx, generate_answer
import uuid, os

SESSION_FILE_KEY = "uploaded_file"
SESSION_TEXT_KEY = "uploaded_file_text"

UPLOAD_DIR = "uploads"

def chat_ui(request):
    return render(request, "index.html")


# ---------------- FILE UPLOAD ----------------
def upload_file(request):
    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"]

        if not os.path.exists(UPLOAD_DIR):
            os.makedirs(UPLOAD_DIR)

        filename = f"{uuid.uuid4()}_{file.name}"
        save_path = os.path.join(UPLOAD_DIR, filename)

        # Save uploaded file
        with open(save_path, "wb+") as dest:
            for chunk in file.chunks():
                dest.write(chunk)

        # Save file path
        request.session[SESSION_FILE_KEY] = save_path

        # Extract text
        if file.name.endswith(".pdf"):
            text = extract_text_from_pdf(open(save_path, "rb"))
        elif file.name.endswith(".docx"):
            text = extract_text_from_docx(open(save_path, "rb"))
        else:
            return JsonResponse({"status": "error", "message": "Unsupported file type!"})

        # Store text in session
        request.session[SESSION_TEXT_KEY] = text

        return JsonResponse({
            "status": "success",
            "filename": file.name,
        })

    return JsonResponse({"status": "error"})


# ---------------- ASK QUESTION ----------------
def ask_question(request):
    if request.method == "POST":
        question = request.POST.get("question")
        file_text = request.session.get(SESSION_TEXT_KEY)

        if not file_text:
            return JsonResponse({"status": "error", "message": "Upload a file first!"})

        # Generate AI answer
        answer = generate_answer(file_text, question)

        return JsonResponse({
            "status": "success",
            "answer": answer
        })

    return JsonResponse({"status": "error"})


# ---------------- RESTART ----------------
def restart_chat(request):
    if SESSION_FILE_KEY in request.session:
        del request.session[SESSION_FILE_KEY]

    if SESSION_TEXT_KEY in request.session:
        del request.session[SESSION_TEXT_KEY]

    return JsonResponse({"status": "success"})
