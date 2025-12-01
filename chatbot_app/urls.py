from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat_ui),
    path("upload-file/", views.upload_file, name="upload_file"),
    path("ask/", views.ask_question, name="ask"),
    path("restart/", views.restart_chat, name="restart"),
]
