
# it will only run whre playwright is installed

from chatgpt_wrapper import ChatGPT

bot = ChatGPT()
# return the full result
bot.ask("give me only chemical reaction for the production of Epoxy resin in one line")
bot.ask("convert above reaction into grams of chemicals required to produce 1 kg of epoxy resin")
response=bot.ask("convert above visualisation into csv file with columns: reactants and  grams required")
print(response)

# # return the result in streaming (chunks)
#for chunk in bot.ask_stream("convert above visualisation into csv file"): 
#   print(chunk)