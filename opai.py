# https://developers.facebook.com/apps/227272759659601/whatsapp-business/wa-dev-console/?business_id=1257043008550008

from flask import Flask, request
import requests
import openai

openai.api_key = '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'

app = Flask(__name__)
 
def send_msg(msg,receiver_number):

   headers = {
       'Authorization': 'Bearer naveenchaurasia',
   }
   json_data = {
       'messaging_product': 'whatsapp',
       'to': receiver_number,
       'type': 'text',
       "text": {
           "body": msg
       }
   }
   response = requests.post('https://graph.facebook.com/LATEST-API-VERSION/PHONE_NUMBER_ID/messages', headers=headers, json=json_data)
   print(response.text)
 

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