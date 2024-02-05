from ollama import Client

while True:
    message=input("Enter a question to ask Llama: ")

    if message.strip().lower()=="exit":
        break

    client = Client(host="http://127.0.0.1:11434")

    completion = client.chat(
        model="llama2",
        messages=[
            {
                'role': 'user',
                'content': message,
            }
        ]
    )

    print(completion["message"]["content"])
    print()