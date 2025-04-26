import openai

response = openai.ChatCompletion.create(

    model="gpt-3.5-turbo",
    
    messages=[{
        "role": "user",
        "content": "Generate 50 diverse examples of daily tasks with due dates, like 'I have a math homework due next Friday'."
    }]
)

print(response.choices[0].message.content)
