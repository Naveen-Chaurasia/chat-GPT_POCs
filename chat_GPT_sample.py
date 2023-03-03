
# it will only run whre playwright is installed
import re
from chatgpt_wrapper import ChatGPT

bot = ChatGPT()
# return the full result
bot.ask("give me only chemical reaction for the production of Epoxy resin in one line")
bot.ask("convert above reaction into grams of chemicals required to produce 1 kg of epoxy resin")
response=bot.ask("convert above visualisation into json file with columns: reactants and  grams required")
#print(response)

#print("*****************************************************************************************")


try :
    # here ; and / are our two markers 
    # in which string can be found. 
    marker1 = '```'
    marker2 = '```'
    regexPattern = marker1 + '(.+?)' + marker2
    str_found = re.search(regexPattern, response).group(1)
except AttributeError:
    # Attribute error is expected if string 
    # is not found between given markers
    str_found = 'Nothing found between two markers'
print(str_found)



# # return the result in streaming (chunks)
#for chunk in bot.ask_stream("convert above visualisation into csv file"): 
#   print(chunk)