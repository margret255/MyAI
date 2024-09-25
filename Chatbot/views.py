from django.shortcuts import render
from django.http import JsonResponse
import openai
import logging

logging.basicConfig(level=logging.DEBUG)
openai.api_key = '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'

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    answer = response['choices'][0]['message']['content'].strip()
    return answer

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')

def index(request):
    return render(request, "index.html")  
