
from chatgpt_wrapper import ChatGPT

bot = ChatGPT()
# return the full result
bot.ask("give me only chemical reaction for the production of Epoxy resin in one line")
bot.ask("convert above reaction into grams of chemicals required to produce 1 kg of epoxy resin")
response=bot.ask("convert above visualisation into csv file with columns: reactants and  grams required")
print(response)


res="Here's an example JSON file representing the chemical reaction for the production of Epoxy resin, with columns for reactants and grams required:
json
Copy code
{
  "reaction": "n(CH2CHCl) + n(C6H4OH) → n(CH2CHOC6H4OH)",
  "reactants": [
    {
      "name": "Epichlorohydrin",
      "formula": "C3H5ClO",
      "molar_mass": 92.52,
      "grams_required_per_kg": 253
    },
    {
      "name": "Bisphenol A",
      "formula": "C15H16O2",
      "molar_mass": 228.29,
      "grams_required_per_kg": 624
    }
  ]
}
Note that the "grams_required_per_kg" value represents the approximate mass of each reactant required to produce 1 kg of epoxy resin, as calculated in the previous answer."
