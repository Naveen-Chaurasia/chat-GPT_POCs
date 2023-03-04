import json

from flask import jsonify
response='''H''ere's an example JSON file that represents the information you requested:

```json
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
```

In this JSON file, the reactants are represented as an array of objects, where each object contains the formula, chemical name, and grams required for the corresponding reactant. The "reactants" array contains three objects for Phenol, Formaldehyde, and Water.

The catalyst information is represented in a separate object, which contains the formula, chemical name, and grams required for the catalyst (in this case, Sodium Hydroxide).

Note that the values for "grams_required" are placeholders and would need to be updated with the correct values based on the specific reaction conditions and quantities.'''

mk1 = response.find('```') +1
mk2 = response.find('```', mk1)
subString = "'"+response[ mk1 : mk2 ] + "'''"

r=subString.replace("`","'")
l=r.replace("json","")

s=l.replace("'","")
#open text file
text_file = open("data.json", "w")

#write string to file
text_file.write(s)

#close file
text_file.close()


print("--------------------------------------------------------------------------------------")

f = open('data.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
print(type(data))

print(s)
print("*****************************************************************************************")
print(type(s))
t =  json.loads(s)
print("--------------------------------------------------------------------------------------")
print(t)
print(type(t))
