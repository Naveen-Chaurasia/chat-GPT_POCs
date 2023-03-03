
# it will only run whre playwright is installed

import json
from promptify.models.nlp.openai_model import OpenAI
from promptify.prompts.nlp.prompter import Prompter
from pprint import pprint
from IPython.display import Markdown, display
from IPython.core.display import display, HTML
from chatgpt_wrapper import ChatGPT

chemical=input("Give the chemical Name: ")
bot = ChatGPT()
# return the full result
bot.ask("give me only chemical reaction for the production of"+chemical+"in one line")
bot.ask("convert above reaction into grams of chemicals and catalyst required to produce 1 kg of"+chemical+".")
response=bot.ask("convert above visualisation into json file with columns: reactants, reactant's name and  grams required")
# print(response)

# # return the result in streaming (chunks)
#for chunk in bot.ask_stream("convert above visualisation into csv file"): 
#   print(chunk)

# Define the API key for the OpenAI model
api_key  = "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"


# Create an instance of the OpenAI model, Currently supporting Openai's all model, In future adding more generative models from Hugginface and other platforms
model = OpenAI(api_key)
nlp_prompter = Prompter(model)

# Named Entity Recognition with No labels, no description, no oneshot, no examples
# Simple prompt with instructions
# domain name gives more info to model for better result generation, the parameter is optional
# Output will be python object -> [ {'E' : Entity Name, 'T': Type of Entity } ]


result = nlp_prompter.fit('ner.jinja',
                          domain      = 'medical',
                          text_input  = response, 
                          labels      = None)

# Output
pprint(eval(result['text']))

print("*****************************************************************************************")
# Summarization with No labels, no description, no oneshot, no examples
# Simple prompt with instructions
# domain name gives more info to model for better result generation, the parameter is optional

result = nlp_prompter.fit('summary.jinja',
                                      text_input=response,
                                      domain="chemical",
                                      token_length = None
                                     )


pprint(eval(result['text']))

print("*****************************************************************************************")

result = nlp_prompter.fit('explain.jinja',
                                      text_input=response,
                                      domain="chemical",
                                      token_length = None
                                     )

pprint(eval(result['text']))
