import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')  

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ],
    max_tokens=150,
)

print(response['choices'][0]['message']['content'])







from django.shortcuts import render
from django.http import JsonResponse
import openai
import logging
import os


logging.basicConfig(level=logging.DEBUG)

openai.api_key = os.getenv('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')

def ask_openai(message):
    try:
        logging.debug(f"Sending message to OpenAI: {message}")
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[{"role": "user", "content": message}],
            max_tokens=150,
            temperature=0.8,
        )
        
        logging.debug(f"OpenAI response: {response}")

        if response['choices'] and isinstance(response['choices'], list):
            answer = response['choices'][0]['message']['content'].strip()
            logging.debug(f"Extracted answer: {answer}")
        else:
            answer = "No valid choices found in response"
        
        return answer
    except Exception as e:
        logging.error(f"API call failed: {e}")
        return "Error connecting to the API"

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        logging.debug(f"Received message from user: {message}")
        
    
        response = ask_openai(message)  
        
        logging.debug(f"Response from ask_openai: {response}")
        return JsonResponse({'message': message, 'response': response})
    
    return render(request, 'chatbot.html')
