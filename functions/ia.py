def ia(pergunta):

    import os

    from groq import Groq

    client = Groq(
        api_key="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",
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": pergunta,
            }
        ],
        model="llama3-8b-8192",
    )

    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content
