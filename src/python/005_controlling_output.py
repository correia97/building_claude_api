from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-20250514"

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)
    print(f"--------------\r\nUser: {text}")

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)
    print(f"--------------\r\nAssistant: {text}")

def chat(messages, system=None, temperature=0.7, stop_sequences=[]):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
        "stop_sequences": stop_sequences,
       }
    
    if system:
        params["system"] = system
    

    message = client.messages.create(**params)
    return message.content[0].text

messages = []
# Exemplo 1 - Controlando a saída com mensagens do sistema
# add_user_message(messages, "Is tea or coffee better at breakfast?")
# add_assistant_message(messages,"Coffee is better because")

#exemplo 2 - Controlando a saída com stop sequences
add_user_message(messages, "Count from 1 to 10")
answer = chat(messages, stop_sequences=["5"])
print(f"--------------\r\nAssistant: {answer}")