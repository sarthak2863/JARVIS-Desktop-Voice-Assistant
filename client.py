from openai import OpenAI

client = OpenAI(
    # api_key="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"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a Virtual assistant named Jarvis, skilled in general skills like Alexa and Google Cloud."},
        {"role": "user", "content": "What is Python programming?"}
    ]
)

print(completion.choices[0].message.content)
