
# it will only run whre playwright is installed
from flask import jsonify,Flask
import json
from chatgpt_wrapper import ChatGPT
import jellyfish

app = Flask(__name__)

bot = ChatGPT()

# chemical=input("Give the chemical Name: ")

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
       #print(type(jsonify({'data': max_sim_row,'score':maxdis})))     
       return jsonify({'data': max_sim_row,'score':maxdis}) 



@app.route('/ab/<string:num>', methods = ['GET'])  
def readcsvfile(chemical):
    bot.ask("give me only chemical reaction for the production of "+chemical+" in one line")
    bot.ask("convert above reaction into kilo grams of chemicals and catalyst required to produce 1 kg of "+chemical+".")
    response=bot.ask("convert above visualisation into json file with columns: reactants formulae, reactant's chemical name and  grams required")

    mk1 = response.find('```') +1
    mk2 = response.find('```', mk1)
    subString = "'"+response[ mk1 : mk2 ] + "'''"

    r=subString.replace("`","'")
    l=r.replace("json","")
    s=l.replace("'","")
    text_file = open("data.json", "w")
    text_file.write(s)
    text_file.close()

    f = open('data.json')
    data = json.load(f)
    
    print(type(data))

    print(s)
    print(type(s))
    t =  json.loads(s)
    print(t)
    print(type(t))
    print (len(t['reactants']))
    print("--------------------------------------------------------------------------------------")

    gwp_sum=0
    for i in range(0,len(t['reactants'])):
        print(t['reactants'][i]['name'])
        print(type(similarity_lcia(t['reactants'][i]['name'])).json) 
        #  print(type((similarity_lcia(t['reactants'][i]['name'])).json())) 
        #return similarity_lcia(t['reactants'][i]['name']).json['data']
        m=similarity_lcia(t['reactants'][i]['name']).json['data']
        print(m[7])
        n=float(m[7])

        gwp_sum= gwp_sum + n


    print (gwp_sum)   
    return str(gwp_sum)


# driver function
if __name__ == '__main__':
  
    app.run(debug = True)