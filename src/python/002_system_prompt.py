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
    system_prompt  ="""
                        You are a patient math tutor.
                        Do not directly answer a student's questions.
                        Guide them to a solution step by step.
                        """

    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    system=system_prompt
    )
    return message.content[0].text

messages = []
add_user_message(messages, "How do I solve 5x+3=2 for x")
response = chat(messages)

print(response)