

import json
import jellyfish  
import csv
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

def similarity_lcia(chem):
    with open("D:\Ardhi\Ecoinvent\cut-off-system-model\Cut-off Cumulative LCIA v3.9.csv", 'r') as file:
       csvreader = csv.reader(file)
       maxdis=0
       max_sim_row=[]
       for row in csvreader:
           dis=jellyfish.jaro_distance(chem, str(row[3]))
           if(dis>maxdis):
            maxdis=dis
            max_sim_row=row
       return jsonify({'data': max_sim_row,'score':maxdis}) 




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
print (len(t['reactants']))


gwp_sum=0
# print(t['reactants'][1]['name'])
for i in range(0,len(t['reactants'])):
   print(t['reactants'][i]['name'])

   gwp_sum= gwp_sum + similarity_lcia(t['reactants'][i]['name'])['data'][7]


print (gwp_sum)   
   


