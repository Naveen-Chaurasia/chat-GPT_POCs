import requests

headers = {
       'Authorization': 'Bearer EAADOtBAbTFEBAAJ1ZBha8zCzn9eXHZBoA5OZB1FfOEbZCKhFBNRAw6GWG5gIGghXhEwrSN1GklyVMzOTW94VGOY4aBNQz7YPI4qtzMkplIZBNqdRURipsm89DISJxX4yb8NTmjC9ClEgZB3uQySMGUahx1e4ZAAq39RWFhiZAkZBrZAQ888CVBB8gTKAZCgM8iRZBNPm2WYxh2PtVQZDZD',
   }

response = requests.post('https://graph.facebook.com/v16.0/103538419355832/messages',
                         json={
       "messaging_product": "whatsapp",
       "to": 919569541918,
       "type": "text",
       "text": {
           "body": "hello buddy"
       }
   },
                         headers=headers)

print("Status code: ", response.status_code)

# response_Json = response.json()
# print("Printing Post JSON data")
# print(response_Json['data'])

# print("Content-Type is ", response_Json['headers']['Content-Type'])
print(response)



# import requests

# auth_token='EAADOtBAbTFEBAAJ1ZBha8zCzn9eXHZBoA5OZB1FfOEbZCKhFBNRAw6GWG5gIGghXhEwrSN1GklyVMzOTW94VGOY4aBNQz7YPI4qtzMkplIZBNqdRURipsm89DISJxX4yb8NTmjC9ClEgZB3uQySMGUahx1e4ZAAq39RWFhiZAkZBrZAQ888CVBB8gTKAZCgM8iRZBNPm2WYxh2PtVQZDZD'
# hed = {'Authorization': 'Bearer ' + auth_token}
# data = {
#        "messaging_product": "whatsapp",
#        "to": 919569541918,
#        "type": "text",
#        "text": {
#            "body": "hello buddy"
#        }
#    }

# url = 'https://api.xy.comhttps://graph.facebook.com/v16.0/103538419355832/messages'
# response = requests.post(url, json=data, headers=hed)
# print(response)
# print(response.json())