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

message={
    'role': 'assistant',
    'content': chat_completion.choices[0].messages.content
}
messages.append(messages)
print(f'Jarvis:{message['content']}')

if __name__ == "__main__":
    user_question=input('Hi im Jarvis, ask me anything')
    completion(user_question)
