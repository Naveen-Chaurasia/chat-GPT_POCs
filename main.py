
# it will only run whre playwright is installed

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
# find() method will search the 
# given marker and stores its index 
mk1 = response.find('```') + 3
# find() method will search the given 
# marker and sotres its index
mk2 = response.find('```', mk1)
# using slicing substring will be 
# fetched in between markers.
subString = response[ mk1 : mk2 ]
print(subString)

# # return the result in streaming (chunks)
#for chunk in bot.ask_stream("convert above visualisation into csv file"): 
#   print(chunk)