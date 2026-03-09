from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-0"

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)
    print(f"--------------\r\nUser: {text}")

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)
    print(f"--------------\r\nAssistant: {text}")

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text


messages = []

while True:

    user_input = input("> ")
    print(">", user_input)

        
    # Add the initial user question
    add_user_message(messages, user_input)

    # Get Claude's response
    answer = chat(messages)

    # Add Claude's response to the conversation history
    add_assistant_message(messages, answer)

    print("-----")
    print(answer)
    print("-----")