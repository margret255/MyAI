import openai

openai.api_key = ''

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello, how are you?"}]
    )
    print(response['choices'][0]['message']['content'])
except Exception as e:
    print(f"Error: {e}")

