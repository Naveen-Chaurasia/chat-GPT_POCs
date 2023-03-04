import json
emoloyees_string ='''
{
  "reactants": [
    {
      "formula": "C6H5OH",
      "name": "Phenol",
      "grams_required": 1000
    },
    {
      "formula": "CH2O",
      "name": "Formaldehyde",
      "grams_required": 1300
    },
    {
      "formula": "H2O",
      "name": "Water",
      "grams_required": 0
    }
  ],
  "catalyst": {
    "formula": "NaOH",
    "name": "Sodium Hydroxide",
    "grams_required": 20
  }
}
'''
print(type(emoloyees_string))

data = json.loads(emoloyees_string)

print(type(data))
#output
#<class 'dict'>
