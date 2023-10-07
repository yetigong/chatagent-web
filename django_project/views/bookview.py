# myapp/views.py
from django.shortcuts import render
import requests

def book_list(request):
    api_url = 'https://chatagent.replit.app/chatagent'  # Replace with your API URL
    payload = {"human_input": "help me to summary for the storyline between 相柳 and 小夭 in 1000 words in Chinese"}
    response = requests.post(api_url, json=payload)
    print(response.json())
    message = response.json().get("output")
    return render(request, 'books.html', {'output': message})