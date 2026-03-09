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

def v1_stream():
    messages = []
    add_user_message(messages, "Write a 1 sentence description of a fake database")

    stream = client.messages.create(
            model=model,
            max_tokens=1000,
            messages=messages,
            stream=True
        )

    for event in stream:
            print(event)



messages = []
add_user_message(messages, "Write a 1 sentence description of a fake database")

with client.messages.stream(
        model=model,
        max_tokens=1000,
        messages=messages
    ) as stream:
        for text in stream.text_stream:
            # Send each chunk to your client
            #print(text, end="")

            # This get only de final response, not the stream
            pass
        final_message = stream.get_final_message()
        print(final_message)