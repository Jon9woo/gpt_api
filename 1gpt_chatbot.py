from openai import OpenAI
from dotenv import load_dotenv
import os

# 환경변수를 불러옴
load_dotenv()

os.environ.get("OPEN_API_KEY")

# api_key를 불러옴
api_key = os.environ.get("OPEN_API_KEY")
client = OpenAI(
    api_key= api_key
)


messages = []
while True:
    content = input("사용자: ")
    messages.append({"role": "user", "content": content})

    complation = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        #model = "gpt-4-turbo",
        messages = messages
    )

    chat_response = complation.choices[0].message.content
    print(f"ChatGPT : {chat_response}")
    messages.append({"role": "assistant", "content": chat_response})