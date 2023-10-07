# mychatapp/views.py
from django.shortcuts import render, redirect
from django_project.models.models import ChatMessage
import requests

def chat(request):
    messages = ChatMessage.objects.all()
    return render(request, 'chat.html', {'messages': messages})

def post_message(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        message = request.POST.get('message')

        # send the requests to the backend
        api_url = 'https://chatagent.replit.app/chatagent'  # Replace with your API URL
        payload = {"human_input": message}
        response = requests.post(api_url, json=payload)
        print(response)
        output = response.json().get("output")
      
        ChatMessage.objects.create(user=user, message=message, response=output)

    print("outside of if")
    return redirect('chat')