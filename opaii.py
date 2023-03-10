from flask import Flask, request
import requests
import openai

openai.api_key = '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'

app = Flask(__name__)
 
def send_msg(msg,receiver_number):

  headers = {
       'Authorization': 'Bearer EAADOtBAbTFEBAD24wHIyxhhy8gkYt0uk1ZAmuZBxWfUK7ZBKVmZAutaqiBwEVGeYYyDH7qxNJ11C0myjJESxIqi0xCf3rU6z17LLxLxE1MZC0SBzHsXDKDsNqrqYRoHG7nNW4WmzRC85aOchSzn7VExaVwYU23qVORLikJ0d5QiZC3OAxNDZC6shN08OgGleNrbidSF62gSYgZDZD',
   }

  response = requests.post('https://graph.facebook.com/v16.0/103538419355832/messages',
                            json={
        "messaging_product": "whatsapp",
        "to": 919569541918,
        "type": "text",
        "text": {
            "body": msg
        }
    },
                            headers=headers)

  print("Status code: ", response.status_code)

  print(response)

@app.route('/receive_msg', methods=['POST','GET'])
def webhook():
   res = request.get_json()
   print(res)
   try:
       if res['entry'][0]['changes'][0]['value']['messages'][0]['id']:
            chat_gpt_input=res['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
            completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": chat_gpt_input}]
            )
            response = completion['choices'][0]['message']['content']
            print("ChatGPT Response=>",response)
            receiver_number=res['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']
            send_msg(response,receiver_number)
   except:
       pass
   return '200 OK HTTPS.'
 
  
if __name__ == "__main__":
   app.run(debug=True)