import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_bot_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert travel guide for India."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']
