import os
from openai import OpenAI

key= "YOUR-API-KEY"

messages = []


client = OpenAI(
    # This is the default and can be omitted
    api_key=key,
)
def completion(message):
    global messages
    messages.append(
        {
            'role': 'user',
            'content': message
        }
    )

    chat_completion=client.chat.completions.create(messages=messages,

    model="gpt-4o"
    )
    print(chat_completion)

if __name__ == "__main__":
    user_question=input('Hi im Jarvis, ask me anything')
    completion(user_question)
