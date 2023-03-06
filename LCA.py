
# it will only run whre playwright is installed
from chatgpt_wrapper import ChatGPT


bot = ChatGPT()

chemical=input("Give the chemical Name: ")

bot.ask("give me only chemical reaction for the production of "+chemical+" in one line")
bot.ask("convert above reaction into grams of chemicals and catalyst required to produce 1 kg of "+chemical+".")
response=bot.ask("convert above visualisation into json file with columns: reactants, reactant's name and  grams required")
print("*****************************************************************************************")
print (response)
print("*****************************************************************************************")


mk1 = response.find('```') + 7
mk2 = response.find('```', mk1)
subString = response[ mk1 : mk2 ]
print(subString)


