# mychatapp/models.py
from django.db import models

class ChatMessage(models.Model):
    user = models.CharField(max_length=50)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
      app_label = 'django_project'  # Specify the app_label for the model