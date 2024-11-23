from ollama import Client

client = Client(
    host="http://100.110.46.126:5001",
)
response = client.chat(
    # model="llama3.2-vision:90b",
    model="llama3.2-vision",
    messages=[
        {
            "role": "user",
            "content": "Why is the sky blue?",
        },
    ],
)

print(response)
