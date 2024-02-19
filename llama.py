from ollama import Client
from queries import *
import json
from dotenv import load_dotenv
load_dotenv()
import os



conn, cur = create_connection()

if conn is None and cur is None:
    print("[llama] Are you sure the PosgreSQL Server is running?")

else:
    create_table(conn, cur)

    while True:
        message=input("Enter a question to ask Llama2: ")

        if message.strip().lower()=="exit":
            break

        messages_for_today = []

        for stored_message in select_messages_for_today(cur):
            messages_for_today.append(stored_message[0])

        localhost_url="http://127.0.0.1"
        host_url=os.environ.get('HOST_URL')
        port="11434"

        client = Client(host=localhost_url+":"+port)

        model_llama_2_7b="llama2"
        model_llama_2_13b="llama2:13b"
        model_llama_2_70b="llama2:70b"

        user_message = {
            'role': 'user',
            'content': message,
        }

        insert_messages(conn, cur, json.dumps(user_message).replace("\'", "\'\'"))

        messages_for_today.append(user_message)

        completion = client.chat(
            model=model_llama_2_7b,
            messages=messages_for_today
        )

        insert_messages(conn, cur, json.dumps(completion["message"]).replace("\'", "\'\'"))

        print(completion["message"]["content"])

        print()