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

def chat(messages, system=None, temperature=1.0):
    params  ={
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
       "temperature": temperature}
    
    if system:
        params["system"] = system
    

    message = client.messages.create(**params)
    return message.content[0].text

messages = []


add_user_message(messages, "What do you think")
# Low temperature - more predictable
answer = chat(messages, temperature=0.0)
print(f"--------------\r\nAssistant: {answer}")
# High temperature - more creative  
answer = chat(messages, temperature=1.0)
print(f"--------------\r\nAssistant: {answer}")

























