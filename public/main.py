import openai

api_key = "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"
openai.api_key = api_key

def send_message(message_log):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_log,
        max_tokens=3800,
        stop=None,
        temperature=0.7,
    )

    for choice in response.choices:
        if "text" in choice:
            return choice.text
        
    return response.choices[0].message.content

def main():
    message_log = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    file = open('db_main.txt', 'r')
    text = file.read()
    file.close()
    user_input = text
    message_log.append({"role": "user", "content": user_input})
    response = send_message(message_log)
    message_log.append({"role": "assistant", "content": response})
    print(f"{response}")

if __name__ == "__main__":
    main()