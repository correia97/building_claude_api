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


def v1_generate_data():
    messages=[]
    add_user_message(messages, "Generate a very short AWS event bridge rule as json")
    answer = chat(messages)
    print(f"--------------\r\n: {answer}")

def v2_generate_data_structed():
    messages=[]
    add_user_message(messages, "Generate a very short AWS event bridge rule as json")
    add_assistant_message(messages, "```json")
    answer = chat(messages, stop_sequences=["```"])
    print(f"--------------\r\n: {answer}")

messages = []
prompt = """
Generate three different sample AWS CLI commands. Each should be very short"""
add_user_message(messages, prompt)
answer = chat(messages)
answer = answer.strip()
print(f"--------------\r\n: {answer}")



messages = []
add_user_message(messages, prompt)
add_assistant_message(messages, "Here are all three commands in a sigle block without any comments:\n```bash")
answer = chat(messages, stop_sequences=["```"])
answer = answer.strip()
print(f"--------------\r\n: {answer}")



