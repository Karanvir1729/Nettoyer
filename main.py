import openai

if __name__ == '__main__':
    history = ""
    openai.api_key = "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"
    p = input("Hi! Hru?")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=p,
        temperature=0,
        max_tokens=4000,
        top_p=0.7,
        frequency_penalty=1,
        presence_penalty=1
    )
    ai_response = response["choices"][0]["text"]
    print(ai_response)
    history += f"me: {p}\n"
    history += f"friend: {ai_response}\n"
    while p != "bye":
        p = input()
        history += f"me: {p}\n"
        history += "friend:"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=history,
            temperature=0,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=1,
            presence_penalty=1
        )
        ai_response = response["choices"][0]["text"]
        print(ai_response)
        history += f" {ai_response}\n"
