from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are my software engineering coach, who knows I have always wanted to know how to integrate OpenAI into my technical projects."},
        {"role": "user", "content": "I just made my first API request to the OpenAI client! Woohoo!"}
    ]
)

print(completion.choices[0].message)