
# it will only run whre playwright is installed
from flask import jsonify
import json
from chatgpt_wrapper import ChatGPT

bot = ChatGPT()

chemical=input("Give the chemical Name: ")
# return the full result
bot.ask("give me only chemical reaction for the production of "+chemical+" in one line")
bot.ask("convert above reaction into kilo grams of chemicals and catalyst required to produce 1 kg of "+chemical+".")
response=bot.ask("convert above visualisation into json file with columns: reactants formulae, reactant's chemical name and  grams required")
print("*****************************************************************************************")
print (response)
print("*****************************************************************************************")
mk1 = response.find('```') +1
mk2 = response.find('```', mk1)
subString = "'"+response[ mk1 : mk2 ] + "'''"

r=subString.replace("`","'")
l=r.replace("json","")

s=l.replace("'","")

text_file = open("data.json", "w")
text_file.write(s)
text_file.close()


print("--------------------------------------------------------------------------------------")
f = open('data.json')
data = json.load(f)
print(type(data))
print(s)
print("*****************************************************************************************")
print(type(s))
t =  json.loads(s)
print("--------------------------------------------------------------------------------------")
print(t)
print(type(t))