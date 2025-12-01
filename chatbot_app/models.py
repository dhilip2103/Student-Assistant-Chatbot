from django.db import models

# Create your models here.

class ChatModel(models.Model):
    user = models.TextField(null=True, blank=True)
    bot = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user[:30]} ..."
