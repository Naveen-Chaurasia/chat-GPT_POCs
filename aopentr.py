import openai

openai.api_key = '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'
query = "Who won the world series in 2020?"
completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                        {"role": "user", "content": query},
                    
                    ]
            )
print("User prompt ==>", query)
print("ChatGPT response ==>", completion['choices'][0]['message']['content'])